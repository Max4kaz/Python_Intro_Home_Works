# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import choices


def multiplication_numbers(a: int):
    check_list = choices(range(a * 2), k=a)
    print(f"List of random numbers:\n{check_list}")
    multiply_pairs_list = []

    if len(check_list) % 2 == 0:
        multiply_pairs_list = list(range(int(len(check_list) / 2)))
        for i in range(0, int(len(check_list) / 2)):
            multiply_pairs_list[i] = check_list[i] * check_list[len(check_list) - 1 - i]
    else:
        multiply_pairs_list = list(range(int(len(check_list) / 2 + 1)))
        for i in range(0, int(len(check_list) / 2)):
            multiply_pairs_list[i] = check_list[i] * check_list[len(check_list) - 1 - i]
        multiply_pairs_list[int(len(check_list) / 2)] = check_list[int(len(check_list) / 2)]
    return multiply_pairs_list


print(f"Multiplication of list's pairs of numbers:\n{multiplication_numbers(int(input('Please enter any number: ')))}")
