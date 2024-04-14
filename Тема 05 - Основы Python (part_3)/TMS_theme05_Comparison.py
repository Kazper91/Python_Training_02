print('Программа для проверки уникальности содержимого списка чисел. Для выхода введите exit.')

start_program = True

while start_program:
    list_numbers = []

    user_request = input('Желаете ли вы создать собственный список, или использовать базовый список? '
                         'Если свой - введите yes, если базовый список - введите basic:    ')
    if user_request == 'exit':
        exit()
    elif user_request == 'yes':
        list_add = ''
        while list_add != 'done':
            list_add = input('Введите цифру для добавления в список. Для завершения списка введите done:    ')
            if list_add == 'done':
                break
            elif list_add == 'exit':
                exit()
            else:
                list_numbers.append(int(list_add))

    elif user_request == 'basic':
        list_numbers = [1, 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 10]

    print(f'\nВаш список: {list_numbers}')

    result_dict = {}
    for item in list_numbers:
        result_dict[item] = result_dict.get(item, 0) + 1

    clones = {item: count for item, count in result_dict.items() if count > 1}

    if clones:
        print(f'Одинаковые значения: {clones}')
    else:
        print('Ничего похожего не найдено!')
