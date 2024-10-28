#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fraction:
    def __init__(self, first: int = 1, second: int = 1):
        if second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        if first < 0 or second < 0:
            raise ValueError("Числитель и знаменатель должны быть положительными")
        self.first = first
        self.second = second
        self._normalize()

    def _normalize(self):

        gcd = self._greatest_common_divisor(self.first, self.second)
        self.first //= gcd
        self.second //= gcd

    @staticmethod
    def _greatest_common_divisor(a: int, b: int) -> int:

        while b:
            a, b = b, a % b
        return a

    def read(self):
        line = input("Введите дробь в формате числитель/знаменатель: ")
        parts = line.split('/')
        if len(parts) != 2:
            raise ValueError("Неправильный формат ввода. Используйте формат 'числитель/знаменатель'")
        self.first, self.second = map(int, parts)
        if self.second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self._normalize()

    def display(self):
        print(f"{self.first}/{self.second}")

    def ipart(self):
        return self.first // self.second

    def __add__(self, other):

        new_first = self.first * other.second + other.first * self.second
        new_second = self.second * other.second
        return Fraction(new_first, new_second)

    def __sub__(self, other):

        new_first = self.first * other.second - other.first * self.second
        new_second = self.second * other.second
        return Fraction(new_first, new_second)

    def __mul__(self, other):

        new_first = self.first * other.first
        new_second = self.second * other.second
        return Fraction(new_first, new_second)

    def __truediv__(self, other):

        new_first = self.first * other.second
        new_second = self.second * other.first
        return Fraction(new_first, new_second)

    def __eq__(self, other):

        return self.first * other.second == self.second * other.first

    def __lt__(self, other):

        return self.first * other.second < self.second * other.first

    def __str__(self):

        return f"{self.first}/{self.second}"

    @staticmethod
    def make_fraction(first: int, second: int):
        if second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        return Fraction(first, second)


if __name__ == "__main__":

    fraction1 = Fraction.make_fraction(5, 3)
    fraction2 = Fraction.make_fraction(2, 3)

    fraction1.display()
    print("Целая часть дроби:", fraction1.ipart())

    result = fraction1 + fraction2
    print(f"{fraction1} + {fraction2} = {result}")

    result = fraction1 - fraction2
    print(f"{fraction1} - {fraction2} = {result}")

    result = fraction1 * fraction2
    print(f"{fraction1} * {fraction2} = {result}")

    result = fraction1 / fraction2
    print(f"{fraction1} / {fraction2} = {result}")

    print(f"{fraction1} == {fraction2}: {fraction1 == fraction2}")
    print(f"{fraction1} < {fraction2}: {fraction1 < fraction2}")

    fraction3 = Fraction()
    fraction3.read()
    fraction3.display()
    print("Целая часть дроби:", fraction3.ipart())
