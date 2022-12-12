# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import choices


def fill_list(number: int):
    if number <= 0:
        print("Negative value of the number of numbers!")
        return []
    user_list = choices(range(number), k=number)
    return user_list


def find_non_repeat(user_list: list):
    result_list = []
    dictionary_list = {}.fromkeys(user_list, 0)
    for i in user_list:
        dictionary_list[i] += 1
    for j in dictionary_list:
        if dictionary_list[j] == 1:
            result_list.append(j)
    return result_list


init_list = fill_list(int(input('Enter number to form a initial list: ')))
print(f'Initial list of numbers:\n{init_list}')
print(f'List of non-repeating numbers:\n{find_non_repeat(init_list)}')
