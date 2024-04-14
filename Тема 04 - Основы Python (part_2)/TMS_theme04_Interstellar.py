from math import pi

start_program = True

print('Программа для решения задачи "Интерстеллар". Для выхода введите exit.')
print('Считаем длину года на двух планетах, через их радиусы и орбитальные скорости, и сравниваем.')

while start_program:

    first_planet_radius = ''
    first_orbit_velocity = ''
    second_planet_radius = ''
    second_orbit_velocity = ''

    while not first_planet_radius.isdigit():
        first_planet_radius = input('\nВведите радиус первой планеты, млн. км.:    ')
        if first_planet_radius == 'exit':
            exit()

    while not first_orbit_velocity.isdigit():
        first_orbit_velocity = input('Введите орбитальную скорость первой планеты, км/ч:    ')
        if first_orbit_velocity == 'exit':
            exit()

    while not second_planet_radius.isdigit():
        second_planet_radius = input('\nВведите радиус второй планеты, млн. км.:    ')
        if second_planet_radius == 'exit':
            exit()

    while not second_orbit_velocity.isdigit():
        second_orbit_velocity = input('Введите орбитальную скорость второй планеты, км/ч:    ')
        if second_orbit_velocity == 'exit':
            exit()

    first_planet_radius = int(first_planet_radius)
    first_orbit_velocity = int(first_orbit_velocity)
    second_orbit_velocity = int(second_orbit_velocity)
    second_planet_radius = int(second_planet_radius)

    first_year_length = (2 * first_planet_radius * pi) / first_orbit_velocity
    print(f'\nДлина года на первой планете составляет: {round(first_year_length, 6)} лет')

    second_year_length = (2 * second_planet_radius * pi) / second_orbit_velocity
    print(f'Длина года на второй планете составляет: {round(second_year_length, 6)} лет')

    if first_year_length > second_year_length:
        print('\nОчевидно, что длина года на первой планете больше, чем на второй.')
    elif first_year_length == second_year_length:
        print('\nОго, продолжительность одинакова!')
    else:
        print('\nК сожалению, длина года на второй планете всё же больше, чем на первой...')
