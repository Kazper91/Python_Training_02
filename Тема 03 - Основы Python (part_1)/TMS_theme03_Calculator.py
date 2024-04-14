start_program = ''
calculation_request = ('\nКакую операцию вы хотите совершить?'
                       '\n    для сложения укажите +'
                       '\n    для вычитания укажите -'
                       '\n    для умножения укажите *'
                       '\n    для деления укажите /'
                       '\n    для возведения в степень укажите ^ или **'
                       '\nВвод:    ')

while start_program != 'exit':
    print('Для выхода введите exit')

    operation = input(calculation_request)

    if operation == 'exit':
        break

    while operation not in ['+', '-', '*', '**', '/', '^']:
        print('\nВведите операцию из предложенных!')
        operation = input(calculation_request)

    first_number = input('Введите первое целое число:    ')
    if first_number == 'exit':
        break

    while not first_number.isdigit():
        print('Введите, пожалуйста, целое число!')
        first_number = input('Введите первое целое число:    ')

    second_number = input('Введите второе целое число:    ')
    if second_number == 'exit':
        break

    while not second_number.isdigit():
        if second_number == 'exit':
            operation = 'exit'
        print('Введите, пожалуйста, целое число!')
        second_number = input('Введите второе целое число:    ')

    if operation == '+':
        result = int(first_number) + int(second_number)
        print(f'Сумма первого числа ({first_number}) и второго числа ({second_number}) ровна', result, '\n')

    elif operation == '-':
        result = int(first_number) - int(second_number)
        print(f'Разность первого числа ({first_number}) и второго числа ({second_number}) ровна', result, '\n')

    elif operation == '*':
        result = int(second_number) * int(second_number)
        print(f'Произведение первого числа ({first_number}) и второго числа ({second_number}) ровна', result, '\n')

    elif operation == '/' and int(second_number) != 0:
        result = int(second_number) / int(second_number)
        print(f'Деление первого числа ({first_number}) на второе число ({second_number}) ровно', result, '\n')

    elif operation == '^' or '**':
        result = int(second_number) ** int(second_number)
        print(f'Возведение первого числа ({first_number}) '
              f'в степень по второму числу ({second_number}) ровно', result, '\n')

    else:
        print('Деление на 0', '\n')
