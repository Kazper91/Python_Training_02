import math

print ('Программа для решения задания с вычислением сложных математических формул. Для выхода введите exit.')

start_program = True

while start_program:
    x = input('\nВведите значение "x", используемое в уравнениях:    ')
    if x == 'exit':
        exit()

    n = input('Введите значение "n", используемое в уравнениях (макс. число итераций):    ')
    if n == 'exit':
        exit()
    elif int(n) < 7:
        n = 7

    iteration_qty = 1

    sin_x = x - (x ** 3) / math.factorial(3) + (x ** 5) / math.factorial(5) - (x ** 7) / math.factorial(7)

    while iteration_qty <= n:
        if n %
        sin_x

