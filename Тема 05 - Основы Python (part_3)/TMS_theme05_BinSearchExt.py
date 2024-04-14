print('Программа бинарного поиска. Для выхода введите exit.')

start_program = True

while start_program:
    test_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f'Ваш список: {test_list}')

    user_input = int(input('\nВведите число для бинарного поиска в списке (от 1 до 20):    '))

    if user_input >= test_list[0]:
        test_list_start_index = 0
        test_list_end_index = test_list.index(min(test_list)) - 1
    else:
        test_list_start_index = min(test_list)
        test_list_end_index = len(test_list) - 1

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
