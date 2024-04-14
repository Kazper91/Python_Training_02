print('Программа для вывода последовательности Фибоначчи. Для выхода введите exit.')

start_program = True

while start_program:
    limit = input('\nВведите число, до которого необходимо посчитать последовательность:    ')
    if limit == 'exit':
        break

    fibonacci = [1]
    a_previous = 1
    b_previous = 0
    number = 0

    while number <= int(limit):
        number = a_previous + b_previous
        if number > int(limit):
            break

        fibonacci.append(number)
        b_previous = a_previous
        a_previous += (number - a_previous)

    print(f'Последовательность Фибоначчи до искомого числа {fibonacci}')
