import math

print('Программа для вычисления конкретных математических уравнений по теме №4. Для выхода введите exit.')

start_program = True

while start_program:
    a = input('\nВведите значение переменной "a":    ')
    if a == 'exit':
        exit()

    b = input('Введите значение переменной "b":    ')
    if b == 'exit':
        exit()

    x = input('Введите значение переменной "x":    ')
    if x == 'exit':
        exit()

    a = int(a)
    b = int(b)
    x = int(x)

    first_y = a ** 2 / 3 + (a ** 2 + 4) / b + (math.sqrt(a ** 2 + 4)) / 4 + math.sqrt(pow((a ** 2 + 4), 3)) / 4
    print(f'\nПо первому уравнению "y" равен: {first_y}')

    second_y = math.cbrt(math.cos(x ** 2) ** 2 + math.sin(2 * x - 1) ** 2)
    print(f'По второму уравнению "y" равен: {second_y}')

    third_y = math.cos(x) + math.sin(x)
    print(f'По третьему уравнению "y" равен: {third_y}')

    fourth_y = (5 * x) + (x ** 2) * 3 * (math.sqrt(1 + math.sin(x) ** 2))
    print(f'По четвертому уравнению "y" равен: {fourth_y}')
