start_program = True

print('Программа для демонстрации манипуляций с числами (которые как бэ строки). Для выхода введите exit.')

while start_program:
    user_number = input('\nВведите некоторое целое число:    ')
    if user_number == 'exit':
        exit()

    if not user_number.isdigit():
        print('Введено не целое число.')

    count = 0
    sum_count = 0
    step = 0
    last_digit = len(user_number) - 1
    tens = len(user_number) - 2

    while step < len(user_number):
        count = int(user_number[step])
        sum_count += count
        step = step + 1

    print(f'1. Последняя цифра введенного числа: {user_number[last_digit]}')
    print(f'2. Количество десятков введенного числа (прямых): {user_number[tens]}')
    print(f'2.1 Количество десятков введенного числа (всего): {user_number[0:tens + 1]}')
    print(f'3. Сумма цифр введенного числа: {sum_count}')
