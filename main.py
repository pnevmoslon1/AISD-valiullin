import random


def crossover_one_point(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    child = parent1[:point] + parent2[point:]
    return child

def crossover_two_point(parent1, parent2):
    point1 = random.randint(1, len(parent1) // 2)
    point2 = random.randint(len(parent1) // 2, len(parent1) - 1)
    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    return child




def create_chromosome(size):
    res = [random.randint(0, 1) for _ in range(size)]
    res.append(float('inf')) 
    return res


def mutation(chromosome, mutation_rate=5):
    for i in range(len(chromosome) - 1):
        if random.randint(0, 101)< mutation_rate:
            chromosome[i] = 1 - chromosome[i]  

#                  
#     ["Яблоко",50,  52,    0.3, 0.2, 14]


def mark_chromosome(chromosome, values = False):
    kkal, cost, b, f, u = 0, 0, 0, 0,0

    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            kkal+=products[i % product_count][2]
            cost += products[i % product_count][1]
            b +=  products[i % product_count][3]
            f += products[i % product_count][4]
            u +=  products[i % product_count][5]
    if values == False:
        chromosome[-1] = (
    abs(kkal - norm[0]) / norm[0] +
    abs(b - norm[1]) / norm[1] +
    abs(cost - 7000) / 7000
    #abs(f - norm[2]) / norm[2] +
    #abs(u - norm[3]) / norm[3]
)


        #if abs(kkal - norm[0]) <= 500 and abs(b - norm[1]) <= 50 and abs(f - norm[2]) <= 50 and abs(u - norm[3]) <= 250:
        if abs(kkal - norm[0]) <= 500 and abs(b - norm[1]) <= 50 and abs(cost - 7000) <= 1000:
            panteon.append(chromosome)
            mark_chromosome(chromosome, True)
        return chromosome
    else:
        print(kkal, " :: ", cost, " :: ", b, " :: ", f, " :: ", u)


def create_new_gen(chromosomes):
    new_gen = []
    for i in range(len(chromosomes) - 1):
        new_gen.append(crossover_one_point(chromosomes[i], chromosomes[i + 1]))
        new_gen.append(crossover_two_point(chromosomes[i], chromosomes[i + 1]))

    for i in range(len(new_gen)):
        new_gen[i] = mark_chromosome(new_gen[i])
        mutation(new_gen[i])

    new_gen.sort(key=lambda x: x[-1])
    return new_gen[:gen_count]


'''
name, cost, kkal, prot, fat, ugl
1                 34    36    9
'''
products = [
    ["Яблоко", 50, 52, 0.3, 0.2, 14],
    ["Банан", 60, 89, 1.1, 0.3, 23],
    ["Куриная грудка", 200, 165, 31, 3.6, 0],
    ["Рис", 80, 130, 2.7, 0.3, 28],
    ["Молоко", 70, 42, 3.4, 3.3, 5],
    ["Хлеб", 40, 265, 9, 1, 49],
    ["Яйцо", 80, 155, 6.3, 5.3, 0.6],
    ["Сыр", 300, 402, 25, 20, 1.3],
    ["Огурец", 30, 16, 0.7, 0.1, 3.6],
    ["Помидор", 40, 18, 0.9, 0.2, 3.9],
    ["Гречка", 90, 343, 13.3, 3.3, 72],
    ["Картофель", 50, 77, 2, 0.1, 17],
    ["Морковь", 40, 41, 0.9, 0.2, 10],
    ["Капуста", 30, 25, 1.3, 0.1, 5],
    ["Перец", 50, 20, 0.9, 0.2, 4.7],
    ["Творог", 150, 98, 11, 4.3, 3.4],
    ["Кефир", 60, 40, 3.3, 1, 4],
    ["Фасоль", 100, 127, 8.7, 0.5, 22.8],
    ["Грецкие орехи", 500, 654, 15.2, 65.2, 13.7],
    ["Лосось", 300, 206, 22, 13, 0],
    ["Тунец", 250, 132, 28, 1, 0],
    ["Креветки", 400, 99, 24, 0.3, 0.2],
    ["Чечевица", 80, 116, 9, 0.4, 20],
    ["Пшено", 90, 360, 11, 3, 73],
    ["Кукуруза", 70, 96, 3.4, 1.5, 21],
    ["Семена подсолнечника", 600, 584, 20.8, 51.5, 20],
    ["Миндаль", 600, 576, 21.2, 49.9, 21.6],
    ["Кокос", 300, 354, 3.3, 33.5, 15.2],
    ["Авокадо", 150, 160, 2, 15, 9],
    ["Спаржа", 50, 20, 2.2, 0.2, 3.7],
    ["Брокколи", 50, 34, 2.8, 0.4, 6.6],
    ["Шпинат", 30, 23, 2.9, 0.4, 3.6],
    ["Чеснок", 20, 149, 6.4, 0.5, 33],
    ["Имбирь", 20, 80, 1.8, 0.2, 18],
    ["Лук", 30, 40, 1.1, 0.1, 9.3],
    ["Петрушка", 20, 36, 3, 0.8, 6.3],
    ["Базилик", 20, 23, 3.2, 0.6, 2.7],
    ["Мелисса", 20, 30, 1.5, 0.2, 6.2],
    ["Майонез", 100, 680, 0.4, 75, 0.6],
    ["Кетчуп", 50, 100, 1, 0.1, 24],
    ["Соевый соус", 30, 53, 5.5, 0.1, 7.9],
    ["Оливковое масло", 100, 884, 0, 100, 0],
    ["Кунжутное масло", 100, 884, 0, 100, 0],
    ["Мед", 30, 304, 0.3, 0, 82.4],
    ["Сахар", 100, 387, 0, 0, 100],
    ["Соль", 100, 0, 0, 0, 0],
    ["Чай черный", 0, 1, 0, 0, 0],
    ["Кофе", 50, 1, 0, 0, 0],
    ["Вода", 0, 0, 0, 0, 0],
    ["Сок апельсиновый", 100, 45, 0.7, 0.2, 10.4],
    ["Сок яблочный", 100, 46, 0.1, 0.1, 11.5],
    ["Пиво", 500, 43, 0.5, 0, 3.6],
    ["Вино", 150, 85, 0.1, 0, 2.6],
    ["Шампанское", 150, 90, 0.1, 0, 2.5],
    ["Коктейль", 200, 200, 0, 0, 30],
    ["Пудинг", 100, 120, 2, 4, 20],
    ["Мороженое", 100, 207, 3.5, 11, 24],
    ["Шоколад", 100, 546, 4.9, 31, 61],
    ["Конфеты", 100, 400, 0.5, 0.1, 98],
    ["Пирожное", 100, 350, 3, 20, 45],
    ["Торт", 100, 400, 5, 25, 50],
    ["Паста", 100, 131, 5, 1.1, 25],
    ["Лазанья", 100, 150, 7, 8, 15],
    ["Пельмени", 100, 250, 10, 10, 30],
    ["Суп", 100, 50, 2, 1, 8],
    ["Бульон", 100, 15, 1, 0.5, 2],
    ["Каша овсяная", 100, 71, 2.5, 1.4, 12],
    ["Каша гречневая", 100, 92, 3.4, 0.6, 19],
    ["Каша рисовая", 100, 130, 2.7, 0.3, 28],
    ["Каша манная", 100, 105, 3, 0.3, 22],
    ["Каша кукурузная", 100, 90, 3, 1, 19],
    ["Каша перловая", 100, 123, 2.3, 0.4, 28],
    ["Каша ячневая", 100, 100, 3.3, 0.5, 22],
    ["Каша пшеничная", 100, 120, 4, 0.5, 25],
    ["Каша чечевичная", 100, 116, 9, 0.4, 20],
    ["Каша фасолевая", 100, 127, 8.7, 0.5, 22.8],
]

panteon = []

norm = [18000, 525, 500, 2000]
gen_count = 150
product_count = 75
product_count -=1
chromosomes = []
generation = 0


for i in range(gen_count):
    chromosomes.append(create_chromosome(gen_count))

while(len(panteon) < 20):
    generation+=1
    for i in range(gen_count):
        mark_chromosome(chromosomes[i])
    chromosomes = create_new_gen(chromosomes)

print("\nbimbimbambam\n")
panteon.sort(key=lambda x: x[-1])
print(generation)
mark_chromosome(panteon[0], True)
