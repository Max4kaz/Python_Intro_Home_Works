# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

user_input = float(input("Введите вещественное число: "))
sum_number = 0
for i in range(len(str(user_input))):
    # user_input %= 10
    # print(user_input)
    sum_number += round(user_input % 10)
    print(sum_number, i)
    user_input //= 10