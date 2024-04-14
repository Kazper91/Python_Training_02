print('Решение задачи где Маша копит на телефон. Для выхода введите exit.'
      'Маша откладывает некоторую сумму каждый день, кроме воскресенья.')


start_program = True

while start_program:
    price = input('\nВведите сумму, которую желаете накопить:    ')
    if price == 'exit':
        exit()

    income = input('Введите сумму, которую можете откладывать ежедневно:    ')
    if income == 'exit':
        exit()

    budget = int(income)
    days = 1

    while budget < int(price):
        days += 1
        if days % 7 == 0:
            continue
        else:
            budget += int(income)

    print(f'\nЧтобы накопить требуемую сумму в {price} рублей, Маше потребуется {days} дней,'
          f'если она будет каждый день откладывать по {income} рублей, кроме Воскресенья.')
