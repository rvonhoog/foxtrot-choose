inventory = ['maintenceLog', 'lockerLocation','crowbar']
party_list = ['Randy', 'asd']
quick_route = 0
test = 0
final_time = 0

def boss_fight(final_time):
    if final_time <= 30:
        print('You walk until you see a light and a figure sitting at a table\nYou smell the food you ordered, not yet eaten\nWatching fork decend you...\n1. Rush the table\n2. Sneak up on him')
        aa_choice = input()
    elif final_time > 30 and final_time < 50:
        print('You walk until you see a light and a figure sitting at a table\nYou smell the food you ordered, activly being eaten\nWatching fork decend you...\n1. Rush the table\n2. Sneak up on him')
        aa_choice = input()
    else:
        print('You walk until you see a light and a figure sitting at a table\nYou smell the scraps of the food you ordered\nYou...\n1. Rush the table\n2. Sneak up on him')
        aa_choice = input()
        
    if aa_choice == '1' and len(party_list) == 5:
        print('With the strength of the whole party you are able to aprehend the Suspect\nJust as you thought it was Architect Andy\nHe tells you all about the tunnels he built\nYou saved the day, and everyone found their missing packages.')
        inventory.append('end_game')
    elif aa_choice == '1' and len(party_list) < 5:
        print('Without the strength of the whole party you are not able to aprehend the Suspect\nHe slips away through his tunnels he built under the city...\n"You have not see the last of me!", he shouts as his voice fades away.')
        inventory.append('end_game')
    elif aa_choice == '2' and len(party_list) <= 2:
        print('With the small party size you could creep up on the figure\nYou recgonize Architect Andy from his picture\nYou call the authorities and they come and aprehend Andy\nHe shouts about getting revenge\nYou found the missing packages and saved the day')
        inventory.append('end_game')
    elif aa_choice == '2' and len(party_list) > 2:
        print('Your party is too large to sneak up\nHe slips away through his tunnels he built under the city...\n"You have not see the last of me", he shouts as his voice fades away.\nYou found the missing packages and saved the day\nfor now....')
        inventory.append('end_game')
    else:
        print('No time to waste!!')
        print("Please enter one of the above numbers")
        

while 'end_game' not in inventory:
    boss_fight(final_time)


print('\n\n\n\n\n\n\nTHE END')
        


print("Party: ", party_list)
print("Inventory: ", inventory)
print("Final Time: ", final_time)
