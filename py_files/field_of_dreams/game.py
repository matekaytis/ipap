import random
import re


class Game:
    def __init__(self):
        self.b_exit = False
        self.b_error = False
        self.b_next_move = False
        self.b_answer = False
        self.s_welcome = 'Добро пожаловать в игру "Поле чудес"\n'
        self.s_quest = ''
        self.s_answer = ''
        self.s_hidden_answer = ''
        self.s_select_drum = ''
        self.s_now_player = ''
        self.s_player_input = ''
        self.l_drum_points = [str(el) for el in range(350, 1001, 50)]
        self.l_drum_points += ['0', '*2', 'Б', '+', 'П']
        self.l_alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        self.d_question = {
            'Крупный морской рак': 'омар',
            'Итальянский футбольный клуб': 'ювентус',
            'Рассказ Антона Чехова': 'зеркало',
            'Передовая, ведущая часть общественной группы, класса': 'авангард',
            'Устройство для оперативной связи с абонентом': 'пейджер',
            'Буквоед': 'талмудист',
            'Оппонент штрейкбрехера': 'забастовщик',
            'Незаменимая аминокислота': 'аргинин',
            'Помада для волос в виде твердого карандаша': 'фиксатуар',
            'Другое название эпохи Возрождения': 'ренессанс',
        }
        self.d_players = {}
        print(self.s_welcome)

    def func_select_qa(self):
        self.s_quest = random.choice(list(self.d_question.keys()))
        self.s_answer = self.d_question[self.s_quest]
        self.s_hidden_answer = "*" * len(self.s_answer)

    def func_drum_rotate(self):
        self.b_next_move = False
        self.s_player_input = '+'
        while self.s_player_input != '':
            self.s_player_input = ''
            self.s_player_input = input(f'Игрок {self.s_now_player} крутите барабан! (Нажать ENTER)')
            if self.s_player_input == '':
                self.s_select_drum = random.choice(self.l_drum_points)
                break

    def func_show_qa(self):
        print(f'\nВопрос: {self.s_quest}')
        print(f'Ответ: {self.s_hidden_answer}')
        print(f'\nДоступные буквы: {" ".join(self.l_alphabet)}\n')

    def func_guess_word(self):
        self.b_error = False
        if len(self.s_player_input) != len(self.s_answer) and len(self.s_player_input) != 1:
            print('Ошибка! Количество введенных символов не соответствует количеству букв в слове либо одной букве')
            self.b_error = True
        elif (not re.search('[А-я]' * len(self.s_answer), self.s_player_input) and
              not re.search('[А-я]', self.s_player_input)):
            print('Ошибка! Введены символы отличные от русских букв')
            self.b_error = True
        elif len(self.s_player_input) == len(self.s_answer):
            if self.s_player_input == self.s_answer:
                print(f'Слово угадано! Игрок "{self.s_now_player}" победил!')
                self.b_exit = True
            else:
                print(f'Слово не угадано! Переход хода!', end='\n')
                self.b_next_move = True
        else:
            if self.s_player_input in self.s_answer:
                print(f'Буква "{self.s_player_input}" есть в данном слове', end='\n')
                l_word = list(self.s_hidden_answer)
                for i in range(len(self.s_answer)):
                    if self.s_answer[i] == self.s_player_input:
                        l_word[i] = self.s_player_input
                self.s_hidden_answer = ''.join(l_word)
                self.l_alphabet.remove(self.s_player_input)
                self.func_show_qa()
                self.b_next_move = False
            else:
                print(f'Буквы "{self.s_player_input}" нет в данном слове', end='\n')
                self.l_alphabet.remove(self.s_player_input)
                self.b_next_move = True


class Players:
    def __init__(self, s_name):
        self.s_name = s_name
        self.i_points = 0


game = Game()
while True:
    # Объявление игроков
    for s in ['one', 'two', 'third']:
        while True:
            s_name_input = input(f'Введите имя игрока {s}: ')
            if re.search(r'\w+', s_name_input):
                break
        player = Players(s_name_input)
        game.d_players[s] = player
    while True:
        game.func_select_qa()
        game.func_show_qa()
        # Игра
        while True:
            for s_key in list(game.d_players.keys()):
                game.s_now_player = game.d_players[s_key].s_name
                game.b_next_move = False
                while not game.b_next_move:
                    game.func_drum_rotate()
                    print(f'Сектор "{game.s_select_drum}" на барабане')
                    if game.s_select_drum == 'Б':
                        game.d_players[s_key].i_points = 0
                        game.b_next_move = True
                    elif game.s_select_drum == '0':
                        game.b_next_move = True
                    elif game.s_select_drum == '+':
                        game.b_next_move = False
                    elif game.s_select_drum == '*2':
                        while True:
                            game.func_show_qa()
                            game.s_player_input = input('Введите букву или слово целиком: ')
                            game.func_guess_word()
                            if not game.b_error:
                                break
                    else:
                        while True:
                            game.func_show_qa()
                            game.s_player_input = input('Введите букву или слово целиком: ')
                            game.func_guess_word()
                            if not game.b_error:
                                break

                if game.b_answer:
                    break
            if game.b_answer:
                break
        # Новая игра?
        s_input = input('Новая игра? y/n ')
        if s_input not in ('y', 'n'):
            game.b_answer = False
            print("Ошибка! Введите либо 'y' либо 'n'!")
        elif s_input == 'y':
            break
        else:
            game.b_exit = True
            break
    if game.b_exit:
        break
