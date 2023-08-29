def check_input(num):
    try:
        num = int(num)
        if num == 4 or num == 6:
            return num
        else:
            print('Ошибка! Введено число ни 4, ни 6')
            return None 
    except:
        print('Ошибка! Введено не число')
        return None
        
def search_lucky(num):
    all_tickets = []
    lucky_numbers = []
    all_numbers = range(10**num)
    last_ticket = str((all_numbers[::-1])[0])
    len_numbers = len(last_ticket)
    
    for i in all_numbers:
        number = str(i)
        if len(number) < len_numbers:
            add_zero = '0' * (len_numbers - len(number))
            ticket_number = add_zero + number
            all_tickets.append(ticket_number)
        else:
            all_tickets.append(number)
            
    first_num = range(int(len_numbers / 2))
    last_num = range(int(len_numbers))[int(len_numbers / 2):int(len_numbers)]
    
    for i in all_tickets:
        sum1 = 0
        sum2 = 0
        for x1 in first_num:
            sum1 += int(i[x1])
        for x2 in last_num:
            sum2 += int(i[x2])
        if sum1 == sum2:
            lucky_numbers.append(i)
    return lucky_numbers

 
try:
    while True:
        num = input('Сколько цифр в билете? (Введите число 4 или 6)\n')
        result = check_input(num)
        if result:	
            all_lucky = search_lucky(result)
            print('Общее число счастливых билетов равно ' + str(len(all_lucky)))
            while True:
                answer = input('Показать их? Введите "да", если ответ - да, или "нет", если ответ нет.\n')
                if answer == 'да':
                    list_ticket = ';\n'.join(all_lucky)
                    print(list_ticket)
                    break
                if answer == 'нет':
                    print('Программа завершена.')
                    break
                else:
                    print('Ошибка! Повторите ввод!')
            break
except:
    print('Application error')
