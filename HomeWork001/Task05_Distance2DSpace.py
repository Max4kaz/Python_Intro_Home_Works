# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

xA = int(input('Введите координату X точки A: '))
yA = int(input('Введите координату Y точки A: '))
xB = int(input('Введите координату X точки B: '))
yB = int(input('Введите координату Y точки B: '))

distanceAB = ((xB - xA)**2 + (yB - yA)**2)**0.5
print(round(distanceAB, 3))