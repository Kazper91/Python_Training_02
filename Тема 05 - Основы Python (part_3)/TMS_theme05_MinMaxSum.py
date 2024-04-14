print('Программа для поиска минимального, максимального значений из списка и их сумму. Для выхода введите exit.'
      'Вводите цифры для добавления в список. Для завершения добавления введите end.')


start_program = True
user_list = []

while start_program:
    user_input = input('Введите число для добавления в список:    ')
    if user_input == 'exit':
        exit()
    elif user_input == 'end':
        print(f'Минимальное значение в списке: {min(user_list)}')
        print(f'Максимальное значение в списке: {max(user_list)}')
        print(f'Сумма чисел в списке: {sum(user_list)}')
        break
    else:
        user_list.append(int(user_input))
