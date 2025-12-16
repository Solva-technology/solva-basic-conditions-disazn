def ask_for_age():
    """
    Задание 1:
    Запросите у пользователя возраст с помощью input().
    Если возраст больше или равен 18, выведите "Вы совершеннолетний".
    В противном случае — "Вы несовершеннолетний".
    """
    age = int(input('Напишите сколько вам лет: '))
    if age >= 18:
        print('Вы совершеннолетний')
    else:
        print('Вы несовершеннолетний')

    # тут выдает мне ошибку из-за "age >= 18", типа нельзя сравнивать строку и числа, если будет время потыкай.

def check_password():
    """
    Задание 2:
    Запросите у пользователя пароль.
    Если введенный пароль равен "secret", выведите "Пароль верный".
    Иначе — "Пароль неверный".
    """
    password = input('Введите пароль: ')
    if password == 'secret':
        print('Пароль верный')
    elif password != 'secret':
        print('Пароль неверный')
    elif password == int:
        print('Пароль неверный')
    else:
        print('Введите пароль заново')


def check_temperature():
    """
    Задание 3:
    Запросите у пользователя температуру в градусах.
    - Если температура ниже 15, выведите "Холодно".
    - Если температура от 15 до 25 (включительно), выведите "Тепло".
    - Если температура выше 25, выведите "Жарко".
    """
    weather_temperature = int(input("Какая погода сейчас в Алматы: "))

    if weather_temperature < 15:
        print('Холодно')
    elif 15 <= weather_temperature <= 25:
        print('Тепло')
    elif weather_temperature >= 26:
        print('Жарко')
    else:
        pass


def check_login_and_password():
    """
    Задание 4:
    Запросите у пользователя логин, а затем пароль.
    Если логин "admin" И пароль "password123", выведите "Доступ разрешен".
    В противном случае — "Доступ запрещен".
    """

    login = str(input('Введите логин: '))
    password = input('Введите пароль: ')


    if login == 'admin' and password == 'password123':
        print('Доступ разрешен')
    elif login != 'admin' and password != 'password123':
        print('Доступ запрещен')
    else:
        print('Доступ запрещен')

if __name__ == '__main__':
    ask_for_age()
    check_password()
    check_temperature()
    check_login_and_password()
