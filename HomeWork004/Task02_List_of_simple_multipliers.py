# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

def multipliers_list(number: int):
    mult_list = []
    div = 2
    while div <= number:
        if number % div == 0:
            mult_list.append(div)
            number /= div
        else:
            div += 1
    return mult_list


print(f'List of simple multipliers:\n{multipliers_list(int(input("Enter any natural number: ")))}')
