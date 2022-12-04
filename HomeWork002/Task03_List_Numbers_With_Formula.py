# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

user_input = int(input("Enter any number: "))
list_formula = []

for i in range(1, user_input + 1):
    list_formula.append(round((1 + 1 / i) ** i, 3))

print(f'\nThe filling list:\n{list_formula}')
print(f"\nThe sum of list's digits is '{sum(list_formula)}'")
