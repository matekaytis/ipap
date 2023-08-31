NUM_CHAR = 10


def func_exit(var):
	if var == 'выход':
		return 0
	elif not var:
		return 1
	else:
		return var


def func_test_value(var_ftv):
	try:
		var_ftv = float(var_ftv)
		return var_ftv
	except ValueError:
		print('Ошибка! Введено не число!')
		return 'error'


def func_test_command(var_ftc):
	try:
		var_ftc = int(var_ftc)
		if var_ftc in range(1, 6):
			return var_ftc
		else:
			print('Ошибка! Неверная команда!')
			return 'error'
	except ValueError:
		print('Ошибка! Неверная команда!')
		return 'error'


def func_test(var_fe, func):
	var_ft = func_exit(input(var_fe))
	while var_ft != 0:
		if var_ft != 1:
			res = func(var_ft)
			if not res == 'error':
				return res
		else:
			print('Ошибка! Пустой ввод!')
		var_ft = func_exit(input(var_fe))
	else:
		return 0


print('Доступные команды:\n1\t- сложение\n2\t- вычитание\n3\t- умножение\n4\t- деление\n5\t- степень\n\t- выход\n')


while True:
	val_one = (func_test('Введите первое число: ', func_test_value))
	if val_one:
		print(f'Первое значение: {val_one:.0f}')
		val_two = (func_test('Введите второе число: ', func_test_value))
		if val_two:
			print(f'Второе значение: {val_two:.0f}')
			val_com = (func_test('Введите команду: ', func_test_command))
			if val_com:
				print(f'Второе значение: {val_com}')
			else:
				break
		else:
			break
	else:
		break


		