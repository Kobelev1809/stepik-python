from functools import total_ordering


# Напишите определение класса Rectangle
@total_ordering
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == self.comp_value(other)

    def __lt__(self, other):
        return self.area < self.comp_value(other)

    @staticmethod
    def comp_value(other):
        return other.area if isinstance(other, Rectangle) else other


# Ниже код для проверки методов класса Rectangle
r1 = Rectangle(3, 4)
assert r1.width == 3
assert r1.height == 4
assert r1.area == 12
assert isinstance(type(r1).area, property), "Вы не создали property area"

assert r1 > 11
assert not r1 > 12
assert r1 >= 12
assert r1 <= 12
assert not r1 > 13
assert not r1 == 13
assert r1 != 13
assert r1 == 12

r2 = Rectangle(2, 6)
assert r1 == r2
assert not r1 != r2
assert not r1 > r2
assert not r1 < r2
assert r1 >= r2
assert r1 <= r2

r3 = Rectangle(5, 2)
assert not r2 == r3
assert r2 != r3
assert r2 > r3
assert not r2 < r3
assert r2 >= r3
assert not r2 <= r3
print("Good")
