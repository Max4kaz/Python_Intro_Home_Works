# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапазоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

print('Please enter')
value_n = int(input(' - value of N: '))
position_one = int(input(' - position one: '))
position_two = int(input(' - position two: '))
fill_list = list(range(-value_n, value_n + 1))

print(f'\nThe filling list:\n{fill_list}')

if len(fill_list) >= position_one > 0 and len(fill_list) >= position_two > 0:
    print(f"\nMultiplication positions '{position_one}' and '{position_two}' is '{fill_list[position_one - 1] * fill_list[position_two - 1]}'")
else:
    print("\nThere are no values for these positions!")
