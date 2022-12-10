# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
# out
# [4, 2, 4, 9]
# 8

# Замечание к ДЗ:
# Мария Андреева・Преподаватель
# Ссылка должна быть pull-request

from random import sample, choices


def sum_odd_numbers(a: int):
    sum_in_list = 0
    check_list = sample(range(a * 2), k=a)
    print(f"List of random numbers:\n{check_list}")
    for i in range(0, a, 2):
        sum_in_list += check_list[i]
    return sum_in_list


print(f"Sum of list's numbers in odd positions is '{sum_odd_numbers(int(input('Enter any number: ')))}'")
