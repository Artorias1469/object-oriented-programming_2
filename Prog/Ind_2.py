#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Hex:
    MAX_SIZE = 100

    def __init__(self, hex_string: str = "0"):
        self._size = self.MAX_SIZE
        self._count = 0
        self._digits = [0] * self._size
        self._initialize_from_string(hex_string)

    def _initialize_from_string(self, hex_string: str):
        hex_string = hex_string.lstrip("0x")
        hex_length = len(hex_string)

        if hex_length > self._size:
            raise ValueError("Число превышает максимальный размер.")

        for i in range(hex_length):
            self._digits[i] = int(hex_string[hex_length - 1 - i], 16)
            self._count += 1

    def __getitem__(self, index: int) -> int:
        if 0 <= index < self._size:
            return self._digits[index]
        raise IndexError("Индекс вне диапазона")

    def __setitem__(self, index: int, value: int):
        if 0 <= index < self._size and 0 <= value <= 15:
            self._digits[index] = value
            self._count = max(self._count, index + 1)
        else:
            raise IndexError("Индекс вне диапазона или значение не является шестнадцатеричной цифрой")

    def __add__(self, other: 'Hex') -> 'Hex':
        result = Hex()
        carry = 0

        for i in range(max(self._count, other._count) + 1):
            digit_sum = self[i] + other[i] + carry
            carry = digit_sum // 16
            result[i] = digit_sum % 16

        if carry > 0:
            result[result._count] = carry
            result._count += 1

        return result

    def __sub__(self, other: 'Hex') -> 'Hex':
        if self < other:
            raise ValueError("Результат вычитания отрицателен.")

        result = Hex()
        borrow = 0

        for i in range(self._count):
            digit_diff = self[i] - other[i] - borrow
            if digit_diff < 0:
                digit_diff += 16
                borrow = 1
            else:
                borrow = 0
            result[i] = digit_diff

        while result._count > 0 and result[result._count - 1] == 0:
            result._count -= 1

        return result

    def __lt__(self, other: 'Hex') -> bool:
        for i in range(max(self._count, other._count) - 1, -1, -1):
            if self[i] < other[i]:
                return True
            if self[i] > other[i]:
                return False
        return False

    def __str__(self) -> str:
        hex_string = ''.join(hex(self[i])[2:].upper() for i in range(self._count - 1, -1, -1))
        return f"0x{hex_string or '0'}"

    def size(self) -> int:
        return self._size

    def count(self) -> int:
        return self._count


if __name__ == "__main__":
    hex1 = Hex("1A3F")
    hex2 = Hex("2B4")

    print(f"Hex1: {hex1}")
    print(f"Hex2: {hex2}")

    hex_sum = hex1 + hex2
    print(f"Сумма: {hex_sum}")

    hex_diff = hex1 - hex2
    print(f"Разность: {hex_diff}")

    print(f"Hex1 < Hex2: {hex1 < hex2}")
