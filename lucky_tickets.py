def check_input(num):
    try:
        num = int(num)
        if num % 2 == 0:
            return num
        else:
            print('Not an even integer')
            return None 
    except:
        print('Not a integer')
        return None
        
def search_lucky(num):
    all_tickets = range(10**num)
    last_ticket = (all_tickets[::-1])[0]
    return last_ticket
#        str_lt = str(last_ticket)
#       for i in range(n):
#          ticket =str(i)
#           if len(ticket) < len(str_lt):
#                ticke(t = '0'*(len(str_lt)-len(ticket))+str(i)
#               print(ticket)
#            print(sum1,sum2)
 
#try:
num = input('How many digits are on the ticket? (There must be an evem number) ')	
result = check_input(num)
if result:
    print(search_lucky(result)) 
#except:
#	print('Application error')
