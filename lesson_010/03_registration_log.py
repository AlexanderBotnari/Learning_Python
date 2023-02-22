# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код
class NotNameError(BaseException):
    pass


class NotEmailError(BaseException):
    pass


def verify_file(file_name):
    bad_list = []
    good_list = []
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            try:
                name, email, age = line.split(' ')
                try:
                    name_1 = verify_name(name)
                    email_1 = verify_email(email)
                    age_1 = verify_age(age)
                    good_list.append(name_1)
                    good_list.append(email_1)
                    good_list.append(age_1)
                except NotNameError as nne:
                    bad_list.append((nne, 'in line :', line))
                except NotEmailError as nee:
                    bad_list.append((nee, 'in line :', line))
                except ValueError as ve:
                    bad_list.append((ve, 'in line :', line))
            except ValueError as ve_1:
                bad_list.append(f'НЕ присутсвуют все три поля: in line >>>{line}')

    with open('registration_bad.txt', 'w', encoding='utf8') as bad:
        for i in bad_list:
            bad.write(str(i) + '\n')

    with open('registration_good.txt', 'w', encoding='utf8') as good:
        for i in range(len(good_list)):
            if (i + 1) % 3 == 0:
                good.write('\n')
            good.write(str(good_list[i]) + ' ')


def verify_name(name):
    verified_name = str(name)
    if verified_name.isalpha():
        return verified_name
    else:
        raise NotNameError('поле имени содержит НЕ только буквы')


def verify_email(email):
    verified_email = str(email)
    if verified_email.__contains__('@') and verified_email.__contains__('.'):
        return verified_email
    else:
        raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')


def verify_age(age):
    verified_age = int(age)
    if 10 <= verified_age <= 99:
        return verified_age
    else:
        raise ValueError(f'invalid age {verified_age}')


verify_file('registrations.txt')
