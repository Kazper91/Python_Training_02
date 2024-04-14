print('Программа бинарного поиска. Для выхода введите exit.')

start_program = True

while start_program:
    test_list = []

    test_list_first_item = int(input('Введите начальное целое число для формирования списка:    '))
    test_list_last_item = int(input('Введите конечное целое число для формирования списка:    '))

    for new_item in range(test_list_first_item, test_list_last_item, 1):
        test_list.append(new_item)

    print(f'Ваш список: {test_list}')

    test_list_start_index = 0
    test_list_end_index = len(test_list) - 1

    user_input = int(input('\nВведите число для бинарного поиска в списке:    '))

    while test_list_start_index <= test_list_end_index:
        test_list_mid_index = (test_list_start_index + test_list_end_index) // 2
        medium = test_list[test_list_mid_index]

        if user_input == medium:
            print(f'Ура! Нашёлся {user_input} в заданном списке на позиции {test_list_mid_index}')
            break
        elif user_input < medium:
            test_list_end_index = test_list_mid_index - 1
        else:
            test_list_start_index = test_list_mid_index + 1
