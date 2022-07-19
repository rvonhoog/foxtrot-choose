import time

final_time = 0
party_list = ['Randy', 'Carl', 'Patti']
inventory = ['Phone']

def add_sus_map():
    print("Suspicious Map added to inventory")
    inventory.append('Suspicious Map')

def ll_function():
    
    computer_fix_time = 0
    print("You turn on the computer and open a browser\nYou recieve an error on the Screen\nno internet")
    print("1. Check Wifi")
    print("2. Restart Computer")
    cf_first_choice = input("Enter Choice: ")
    
    if cf_first_choice == '2':
        print("You restarted the Computer but the error persists\nTime Added: 5 minutes")
        computer_fix_time += 5

    print("You looked at the Wifi and noticed it is not working\nYou now focus your attention to the Router")
    print("1. Power Cycle Router")
    print("2. Check Cables")

    cf_second_choice = input("Enter Choice: ")
    
    if cf_second_choice == '1':
        print("You Power cycled the Router but the error persists\nTime Added: 6 minutes")
        computer_fix_time += 6
        
    print("You look at the cables to the Router and notice the internet cable is loose.\nYou plug it in correctly and see the Internet Light go back to green!\nTime added: 3 mins")
    
    party_list.append('Lisa')
    print("Lisa is so happy you helped her with the computer, she quickly seraches for the map and joins your party.")
    computer_fix_time += 3
    
    add_sus_map()
    return computer_fix_time

print("You make your way down to the Library and find Lisa.\nYou ask her for any information she has regarding the missing lockers.\nBeing an expert in her field she knows of a map that might be able to help.\nUnfortunately she is very busy and can't help you look because the computers at the Library are all down.\nYou decide to...\n")

while 'Suspicious Map' not in inventory:
    print("1. Search the Location Lisa told you for a map")
    print("2. Help Lisa fix the computer")
    print("3. Go to the coffee shop to get some coffee")
    ll_first_choice = input("Enter Choice: ")

    if ll_first_choice == '1' and len(party_list) > 2:
        print("You, Carl, and Patti all search the book section to find a local map, because your party size is 3 you find it quite fast.")
        print("Time spent: 5 minutes")
        final_time = final_time + 5
        add_sus_map()
    elif ll_first_choice == '1' and len(party_list) == 2:
        print("You and Carl search the book section and find a local map.")
        print("Time spent: 10 minutes")
        final_time = final_time + 10
        add_sus_map()
    elif ll_first_choice == '2':
      print("You have decided to help Lisa troubleshoot the computer.")
      final_time += ll_function()
    elif ll_first_choice == '3' and 'Coffee' not in inventory:
      print("You run to the Coffee shop in the library and stand in line for your coffee.\nYou feel refreshed")
      print("Time spent: 3 minutes")
      final_time = final_time + 3
      inventory.append('Coffee')
    elif ll_first_choice == '3' and 'Coffee' in inventory:
      print("You already got a coffee\nSelect another option.")
      print("Time added: 1 minute")
      final_time = final_time + 1
    else:
      print("You stand still wasting time")
      print("Time added: 2 minutes")
      final_time = final_time + 2

print("Now with the map in your possesion\nYou and your party notice a strange line connecting your apartment building to another\nYou follow the line")

print("Party: ", party_list)
print("Inventory: ", inventory)
print("Final Time: ", final_time)
