# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randint

user_number = int(input('Please enter any number: '))
work_list = list(range(user_number))

print(f'\nThe initial list:\n{work_list}')

for i in range(user_number):
    i_new = randint(0, i + 1)
    work_list[i], work_list[i_new] = work_list[i_new], work_list[i]

print(f'\nThe mixed list:\n{work_list}')
