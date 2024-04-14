import math

print('Расчет площади прямоугольного треугольника и длины гипотенузы. Для выхода введите exit.')

start_program = True

while start_program:
    cat_a = input('\nВведите значение первого катета:    ')
    if cat_a == 'exit':
        exit()

    cat_b = input('\nВведите значение второго катета:    ')
    if cat_b == 'exit':
        exit()


    def tr_calculation(a, b):
        if a.isdigit() and b.isdigit():
            tr_hypotenuse = math.sqrt(pow(int(a), 2) + pow(int(b), 2))
            print(f'Гипотенуза ровна {round(tr_hypotenuse, 2)} единиц')

            tr_square = (int(a) * int(b)) / 2
            print(f'Площадь ровна {round(tr_square, 2)} квадратных единиц')

        elif '.' in a and '.' in b:
            a = float(a)
            b = float(b)
            tr_hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
            print(f'Гипотенуза ровна {round(tr_hypotenuse, 2)} единиц')

            tr_square = (a * b) / 2
            print(f'Площадь ровна {round(tr_square, 2)} квадратных единиц')

        elif ',' in a and ',' in b:
            a = float(a.replace(',', '.'))
            b = float(b.replace(',', '.'))
            tr_hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
            print(f'Гипотенуза ровна {round(tr_hypotenuse, 2)} единиц')

            tr_square = (a * b) / 2
            print(f'Площадь ровна {round(tr_square, 2)} квадратных единиц')

        else:
            print('Вы ввели неподдерживаемые значения, повторите запрос:')
            return


    tr_calculation(cat_a, cat_b)
