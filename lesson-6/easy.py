# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)

    def check_triangle(self):
        lengths = [self.a, self.b, self.c]
        for x in lengths:  # каждая из сторон треугольника должна быть < суммы других 2х сторон
            if x > sum([_ for _ in lengths if _ != x]):
                return False
        return True

    def square(self):
        s = 1 / 2 * abs((self.x2 - self.x1) * (self.y3 - self.y1) -
                        (self.x3 - self.x1) * (self.y2 - self.y1))
        return round(s, 2)

    def height(self):
        s = (self.a + self.b + self.c) / 2
        h1 = 2 * math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) / self.a
        h2 = 2 * math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) / self.b
        h3 = 2 * math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) / self.c

        h = [round(h1, 2), round(h2, 2), round(h3, 2)]
        return h

    def perimeter(self):
        p = self.a + self.b + self.c
        return round(p, 2)


triangle = Triangle(1, 1, 2, 5, 5, 3)
if triangle.check_triangle():
    print("\nЗадача - 1.")
    print("Треугольник.")
    print(f"Площадь: {triangle.square()}")
    print(f"Высоты, опущенные на каждое основание: {triangle.height()}")
    print(f"Периметр: {triangle.perimeter()}\n")
else:
    print("Треугольника не сущесвует\n")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class TrapezeEqual:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def sides_length(self):
        a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        c = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        d = math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
        return [round(a, 2), round(b, 2), round(c, 2), round(d, 2)]

    def find_base(self):
        tmp = self.sides_length()
        base = [_ for _ in tmp if tmp.count(_) < 2]
        return base

    def find_equal_side(self):
        tmp = self.sides_length()
        side = [_ for _ in tmp if tmp.count(_) == 2]
        if side and len(side) != 4:       # не 4 элементов списка, иначе не трапеция
            return side[0]
        else:
            return []

    def check_trapeze(self):
        side = self.find_equal_side()
        if side:                           # есть две одинаковые стороны
            lengths = self.sides_length()
            for x in lengths:              # каждая из сторон четырехугольника должна быть < суммы других 3х сторон
                if x > sum([_ for _ in lengths if _ != x]):
                    return False
        else:
            return False
        return True

    def square(self):
        base = self.find_base()
        h = self.height()
        s = sum(base) / 2 * h
        return round(s, 2)

    def perimeter(self):
        return round(sum(self.sides_length()), 2)

    def height(self):
        base = self.find_base()
        a = base[0]
        b = base[1]
        c = self.find_equal_side()
        h = math.sqrt(c ** 2 - (a - b) ** 2 / 4)
        return h


print("Задача - 2.")
trapeze = TrapezeEqual(-5, -2, -2, 2, 2, 2, 5, -2)
if trapeze.check_trapeze():
    print("Фигура является равнобочной трапецией.")
    print(f"Длины сторон: {trapeze.sides_length()}")
    print(f"Периметр: {trapeze.perimeter()}")
    print(f"Площадь: {trapeze.square()}")
else:
    print("Фигура не является равнобочной трапецией.")
