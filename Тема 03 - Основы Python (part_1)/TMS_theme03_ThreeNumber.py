start_program = True

print('Программа для заданных математических преобразований трёх вводимых чисел. Для выхода введите exit.')

while start_program:
    first_num = input('\nВведите первое число:    ')
    if first_num == 'exit':
        exit()

    second_num = input('\nВведите второе число:    ')
    if second_num == 'exit':
        exit()

    third_num = input('\nВведите третье число:    ')
    if third_num == 'exit':
        exit()

    if first_num.isdigit() and second_num.isdigit() and third_num.isdigit():
        print('Сумма трех чисел ровна:')
        print(int(first_num) + int(second_num) + int(third_num))

        print('Разность трех чисел ровна:')
        print(int(first_num) - int(second_num) - int(third_num))

        print('Произведение трех чисел ровно:')
        print(int(first_num) * int(second_num) * int(third_num))

        print('Если первого числа отнять второе и прибавить третье, то получим:')
        print(int(first_num) - int(second_num) + int(third_num))

        print('Если первое число умножим на второе, а потом поделим на третье, то получим:')
        print(int(first_num) * int(second_num) / int(third_num))

        print('Остаток от деления суммы первых двух чисел на третье равен:')
        print((int(first_num) + int(second_num)) % int(third_num))
    else:
        print('Введены некорректные данные, повторите ввод целых чисел')
