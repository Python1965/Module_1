
# Практическое задание по уроку "Организация программ и методы строк."
# ***************************************************************************************************************
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
# Используя методы строк, выполните следующие действия:
#   - Выведите строку my_string в верхнем регистре.
#   - Выведите строку my_string в нижнем регистре.
#   - Измените строку my_string, удалив все пробелы.
#   - Выведите первый символ строки my_string.
#   - ыведите последний символ строки my_string.
## **************************************************************************************************************

print("Введите произвольный текст:")
my_string = input(">> ")
print("Количество символов строки:", len(my_string))

print(my_string.upper())
print(my_string.lower())

my_string = my_string.replace(' ', '')
print(my_string[0])
print(my_string[-1])
