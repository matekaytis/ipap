MAX_CHAR = 10


class Calc:
    def __init__(self):
        self.b_exit = False
        self.b_error = False
        self.b_repeat = True
        self.i_com = 0
        self.f_res = 0
        self.s_res = ''
        with open('welcome.txt') as f:
            __l_welcome = f.readlines()
        __l_welcome.insert(0, 'Доступные команды:\n')
        __l_welcome.append(f'\nПримечание: максимальное допустимое количество символов - {MAX_CHAR}')
        self.s_txt_welcome = ('\t'.join(__l_welcome)).replace(';', ' - ')
        with open('err_repeat.txt') as f:
            self.s_err_repeat = list(f.readlines())[0]

    def func_input_command(self, s_com):
        if s_com in ('1', '2', '3', '4', '5'):
            self.i_com = int(s_com)
            self.b_error = False
        elif s_com in ('в', 'e'):
            self.b_exit = True
            return 0
        else:
            self.b_error = True
            return 0

    def func_command(self, f_var_one, f_var_two):
        if self.i_com == 1:
            self.f_res = f_var_one + f_var_two
        elif self.i_com == 2:
            self.f_res = f_var_one - f_var_two
        elif self.i_com == 3:
            self.f_res = f_var_one * f_var_two
        elif self.i_com == 4:
            self.f_res = f_var_one / f_var_two
        else:
            self.f_res = f_var_one ** f_var_two

    def func_output(self):
        self.s_res = self.f_res
        #if self.s_res > MAX_CHAR:
        print(f'Результат: {self.s_res}')


class Numbers:
    def __init__(self, s_number):
        self.error = False
        self.exit = False
        self.s_number = s_number
        self.f_number = 0

    def func_input_number(self):
        if len(self.s_number) == 0 or len(self.s_number) > 10:
            self.error = True
            return 0
        else:
            try:
                self.f_number = float(self.s_number)
            except ValueError:
                if self.s_number in ('e', 'в'):
                    self.exit = True
                else:
                    self.error = True
                    return 0


calc = Calc()
while True:
    print(calc.s_txt_welcome)
    while True:
        number_one = Numbers(input('Введите первое число: '))
        number_one.func_input_number()
        if not number_one.error:
            break
    if number_one.exit:
        break
    while True:
        number_two = Numbers(input('Введите второе число: '))
        number_two.func_input_number()
        if not number_two.error:
            break
    if number_two.exit:
        break
    while True:
        calc.func_input_command(input('Введите команду: '))
        if not calc.b_error:
            break
    if calc.b_exit:
        break
    calc.func_command(number_one.f_number, number_two.f_number)
    calc.func_output()
    if input('Новый расчет? (выход - в (рус.) или e (англ.)): ') in ('в', 'e'):
        break
