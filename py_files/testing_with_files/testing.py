import re
import os


PATTERN_FILE = r'^[A-zА-я0-9-_.]*[A-zА-я0-9-_]$'


# Открывает файл для чтения, читает все содержимое и закрывает файл
def func_read_f(n_file):
	try:
		if type(n_file) == str and re.match(PATTERN_FILE, n_file):
			with open(n_file, 'r') as file:
				return file.readlines()
		else:
			print('Ошибка! Некорректный ввод имени файла!')
	except FileNotFoundError:
		print('Ошибка! Файл не найден.')


# Открывает файл для чтения, читает все содержимое и закрывает файл
def func_write_f(n_file, mode_f, content_f):
	if type(n_file) == str and re.match(PATTERN_FILE, n_file):
		if os.path.exists(n_file):
			try:
				with open(n_file, 'r') as file:
					print('')
				print('Проверка прошла успешна. Начинается запись в файл.')
				with open(n_file, 'a') as file:
				 	file.
			except IOError:
				print('Ошибка! Файл уже открыт.')
		else:
			print('Файл не найден. Будет создан новой файл с именем "{}" в текущей папке.'.format(n_file))
	else:
		print('Ошибка! Некорректный ввод имени файла!')


# text_f = func_read_f(input('Введите имя файла: '))
# if text_f:
# 	print(i for i in text_f)
text = 'Пример записи текста в файл'
print(func_write_f(input('Введите имя файла: '), 1, text))
