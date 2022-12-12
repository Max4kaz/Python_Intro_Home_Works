# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

# user_number = Decimal(input("Enter a real number: "))
# print(user_number.quantize(Decimal(input("Enter the required accuracy: "))))


from decimal import Decimal


def calc_accuracy(number, accuracy):
    number_accuracy = number.quantize(Decimal(accuracy))
    return number_accuracy


print(f'Result number with required accuracy: {calc_accuracy(Decimal(input("Enter a real number: ")), Decimal((input("Enter the required accuracy: "))))}')
