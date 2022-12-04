# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

from decimal import Decimal

user_input = Decimal(input("Enter any number: "))
sum_numbers = 0
user_input *= 10 ** (len(str(user_input)) - 2)

for i in range(len(str(user_input))):
    sum_numbers += user_input % 10
    user_input //= 10

print(f"\nThe sum of digits from this number is '{sum_numbers}'")
