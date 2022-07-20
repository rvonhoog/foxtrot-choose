
inventory = ['maintenceLog', 'sus', 'sus', 'sus', 'lockerLocation','craowbar']
party_list = ['Randy', 'Caarl', 'Paatti']
quick_route = 0
test = 0
final_time = 0

print(inventory)

def add_harbor():
    print('harbor added to inventory')
    inventory.append('harbor')

def carl_bonus():
    if 'Carl' in party_list:
        return 10
    else:
        return 20
        
final_time += carl_bonus()

def headquarters():
    print('1. Investigate the back of the lockers')
    print('2. Try to login to the iPad')
    print('3. Look in the truck')
    print('4. Call Support')
    
    headquarters_choice = input('Enter Choice: ')
    
    if headquarters_choice == '1' and 'crowbar' in inventory:
        print('Looks like the lock is old and beaten up...\nYou and your party use the crowbar you found at Home Depot\nYou pop the lock and climb in through the back\nTime Taken: 1 minute')
        add_harbor()
        break_in_time = 1
        
    elif headquarters_choice == '1' and 'crowbar' not in inventory:
        print('Looks like the lock is old and beaten up...\nIf only you had a tool to help you break it\nTime Taken: 2 minute')
        break_in_time = 2
        
    elif headquarters_choice == '2' and 'Patti' in party_list:
        print('Patti is an expert in these lockers\nShe proceeds to open an XL locker...\nYou and your party climb in...\nTime Taken: 1 minute')
        add_harbor()
        break_in_time = 1

    elif headquarters_choice == '2' and 'Patti' not in party_list:
        print('Unfortulatly there is no one in your party that can get into the lockers')
        print("Time added: 2 minutes")
        break_in_time = 2
        
    elif headquarters_choice == '3':
        print('The truck is locked and looks like whoever owns it loves fast food\nTime Taken: 1 minute')
        break_in_time = 1

    elif headquarters_choice == '4':
        print('You call support and explain the issue\nThey place you on a hold')
        print('....')
        print('They have concernes about the missing packages too and pop open the lockers\nYou and your party climb through')
        print("Time added: 7 minutes")
        add_harbor()
        break_in_time = 7
        
    else:
        print("You stand still wasting time")
        print("Time added: 2 minutes")
        break_in_time = 2

    return break_in_time

if quick_route == 1:
    print('You follow Andy down a long road until you see a lone set of harbor lockers in the middle of nowhere\nYou wait for him to park and enter throug the back of the locker bank.')
else:
    print('You follow the instructions down a long road until you see a lone set of harbor lockers in the middle of nowhere\nYou see a lone truck sitting behind the lockers.')
print('When you get to the locker you dont notice anything that unusual...\nbesides an outfited back that lockes from the inside...\nDo you...')


while 'harbor' not in inventory:
    print('ft: ',final_time)
    final_time += headquarters()
    print('ft2: ',final_time)


