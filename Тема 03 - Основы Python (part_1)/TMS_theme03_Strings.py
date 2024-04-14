start_program = True

print('Программа для демонстрации манипуляций со строкой. Для выхода введите exit.')

while start_program:
    user_str = input('\nВведите интересную строку (например "Hello" или "TEST-STR"):    ')
    if user_str == 'exit':
        exit()

    a = len(user_str) - 2
    d = len(user_str)
    rev_string = user_str[::-1]

    print(f'1. Третий символ введенной строки: {user_str[2]}')
    print(f'2. Предпоследний символ введенной строки: {user_str[a]}')
    print(f'3. Первые пять символов строки: {user_str[:5]}')
    print(f'4. Вся строка, кроме последних двух символов: {user_str[0:a]}')
    print(f'5. Все символы с четными индексами: {user_str[::2]}')
    print(f'6. Все символы с нечетными индксами: {user_str[1::2]}')
    print(f'7. Все символы в обратном порядке: {rev_string}')
    print(f'8. Все символы через один в обратном порядке, начиная с последнего: {rev_string[0::2]}')
    print(f'9. Длина строки: {d}\n')
