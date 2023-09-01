NUM_CHAR = 10


def func_exit(var_e):
	if var_e == 'выход':
		return 0
	elif not var_e:
		return 1
	else:
		return var_e


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
		

def func_command(var_a, var_b, var_fc):
	if var_fc  == 1:
		return var_a + var_b
	elif var_fc  == 2:
		return var_a - var_b
	elif var_fc  == 3:
		return var_a * var_b
	elif var_fc  == 4:
		if var_b != 0:
			return var_a / var_b
		else:
			return 'error'
	elif var_fc  == 5:
		return var_a ** var_b

print('Доступные команды:\n1\t- сложение\n2\t- вычитание\n3\t- умножение\n4\t- деление\n5\t- степень\n\t- выход\n')


while True:
	res_t_one = (func_test('Введите первое число: ', func_test_value))
	if res_t_one:
		print(f'Первое значение: {res_t_one:.0f}')
		res_t_two = (func_test('Введите второе число: ', func_test_value))
		if res_t_two:
			print(f'Второе значение: {res_t_two:.0f}')
			res_t_com = (func_test('Введите команду: ', func_test_command))
			if res_t_com:
				res_com = func_command(res_t_one, res_t_two, res_t_com)
				if not res_com == 'error':
					print('Результат: {res_')
			else:
				break
		else:
			break
	else:
		break


		