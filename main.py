# Задание 1.
# Написать рекурсивную функцию нахождения степени числа.
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
result = power(5, 3)
print(result)

# Задание 2.
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером.
def print_stars(n):
    if n > 0:
        print("*", end="")
        print_stars(n - 1)
    else:
        print()

# Пример использования
n = int(input("Enter number N: "))
print_stars(n)
# Задание 3.
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b. Проиллюстрируйте работу функции примером.
def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)

# Пример использования
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
result = sum_range(a, b)
print("Sum of numbers range from", a, "to", b, "equals", result)
# Задание 4.
# Напишите рекурсивную функцию, которая принимает одномерный массив из 100 целых чисел
# заполненных случайным образом и находит позицию, с которой начинается последовательность
# из 10 чисел, сумма которых минимальна.
import random
def find_min_sum_index(numbers, start=0):
    if start + 10 > len(numbers):
        return start

    min_sum_index = find_min_sum_index(numbers, start + 1)
    current_sum = sum(numbers[start:start + 10])
    min_sum = sum(numbers[min_sum_index:min_sum_index + 10])

    if current_sum < min_sum:
        return start
    else:
        return min_sum_index


# Creating an array from 100 random numbers
numbers = [random.randint(1, 100) for _ in range(100)]

# Find the position from which the sequence of 10 numbers with the minimum sum begins
start_index = find_min_sum_index(numbers)

# Getting result
print("The position at which the sequence of 10 numbers with the minimum sum begins:", start_index)



