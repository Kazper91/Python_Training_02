start_program = True

print('Программа для решения задания "Играл с кредитами - проиграл". Для выхода введите exit.')

while start_program:
    i = input('\nВведите годовую процентную ставку, %:    ')
    if i == 'exit':
        exit()

    s = input('Введите сумму займа:    ')
    if s == 'exit':
        exit()

    n = input('Введите количество месяцев, на которые взят кредит:    ')
    if n == 'exit':
        exit()

    i = int(i)             # Годовой процент
    p = int(i) / 100 / 12  # Месячный процент
    s = int(s)             # Сумма займа
    n = int(n)             # Число месяцев

    x = (1 + p) ** n  # Для упрощения счета
    m = round((s * p * round(x, 2)) / (round(x, 2) - 1), 4)
    print(f'\nЕжемесячная выплата составит: {m} денежных единиц')

    total = round((m * n), 4)  # Итого
    print(f'Общая сумма выплат составит: {total} денежных единиц')

    deference = round((total - s), 4)  # Переплата
    print(f'Сумма переплаты составит: {deference} денежных единиц')
