from sklearn.cluster import KMeans
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import pandas as pd

# Константы
BASE_STATIONS = {
    1: {"radius": 1, "capacity": 2000, "cost": 50000},
    2: {"radius": 2, "capacity": 10000, "cost": 180000},
}
MAXIMIZE_PRECENT = 95.0
MAX_AMOUNT_STATIONS = 150

def apply_kmeans(data):
    """
    Кластеризация домов с использованием KMeans.
    """
    kmeans = KMeans(n_clusters=MAX_AMOUNT_STATIONS, init='k-means++', tol=1e-3, max_iter=300, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['latitude', 'longitude']])
    return data, kmeans.cluster_centers_

def assign_stations(data, cluster_centers):
    """
    Назначение базовых станций с учетом ограничений.
    """
    stations = []
    total_coverage = set()
    
    for i, center in enumerate(cluster_centers):
        cluster_houses = data[data['cluster'] == i]
        total_devices = cluster_houses['end_devices_count'].sum()

        station_type = 1 if total_devices <= BASE_STATIONS[1]['capacity'] else 2
        station_radius = BASE_STATIONS[station_type]['radius']

        selected_house = None
        for _, house in cluster_houses.iterrows():
            house_coords = (house['latitude'], house['longitude'])
            center_coords = (center[0], center[1])
            if geodesic(house_coords, center_coords).km <= station_radius:
                selected_house = house
                break
            
        print(f"[{i}/{len(cluster_centers)-1}] Create Stations.")
        if selected_house is not None:
            stations.append({
                "house_uuid": selected_house['house_uuid'],
                "type": station_type,
            })
    return stations, total_coverage

def calculate_coverage(houses, centers, radius):
    covered_houses = set()
    for center in centers:
        for _, house in houses.iterrows():
            if geodesic(center, house['coordinates']).km <= radius:
                covered_houses.add(house['house_uuid'])
    return covered_houses

def start(path_input_data="house.csv"):
    data_file = path_input_data
    data = pd.read_csv(data_file, delimiter=';')
    data['coordinates'] = data[['latitude', 'longitude']].apply(tuple, axis=1)

    data, cluster_centers = apply_kmeans(data)

    stations, total_coverage = assign_stations(data, cluster_centers)

    output_data = pd.DataFrame(stations)
    output_data.to_csv("output_stations.csv", sep=';', index=False)
    draw_stations(data, stations)
    print(f"[{len(total_coverage)/len(data['house_uuid'])*100}%] Coverage.")
    print("[+] Результаты сохранены в output_stations.csv")

def draw_stations(data, stations):
    result_df = pd.read_csv("output_stations.csv", sep=';')

    # Чтение координат всех домов
    houses_df = pd.read_csv("house.csv", sep=';')
    houses_df.dropna(inplace=True)

    # Объединение данных о станциях с координатами домов
    merged_df = result_df.merge(houses_df, how="left", left_on="house_uuid", right_on="house_uuid")

    # Создание графика
    fig, ax = plt.subplots(figsize=(12, 8))



    # Отображение базовых станций
    bs_1 = merged_df.query("type == 1")
    bs_2 = merged_df.query("type == 2")

    ax.scatter(bs_1["longitude"], bs_1["latitude"], marker='o', color='blue', label='Базовая станция типа 1')
    ax.scatter(bs_2["longitude"], bs_2["latitude"], marker='x', color='red', label='Базовая станция типа 2')
    # Отображение всех домов
    ax.scatter(merged_df["longitude"], merged_df["latitude"], marker='*', color='green', label='Дома')

    # Отображение всех домов

    for station in stations:
        house_uuid = station['house_uuid']
        station_type = station['type']
        house_data = data[data['house_uuid'] == house_uuid]
        plt.scatter(
            house_data['longitude'],
            house_data['latitude'],
            color='red' if station_type == 1 else 'blue',
            marker='^',  
            s=100, 
            label=f'Station Type {station_type}',
        )

    plt.title("Расположение домов и базовых станций")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.savefig("output_plot.png") 
    plt.close()


# Запуск функции
start()
