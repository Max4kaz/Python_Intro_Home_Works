# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

user_input = int(input("Enter any number: "))
list_mult = []
mult_numbers = 1

for i in range(1, user_input + 1):
    mult_numbers *= i
    list_mult.append(mult_numbers)

print(f'\nMultiplication of numbers from 1 to {user_input} in list:\n{list_mult}')
