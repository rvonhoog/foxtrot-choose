import time
import random

inventory = []
party_list = ['randy']
final_time = 0
quick_route = 0

print("You wake up to a notification on your phone, your package has arrived at the lockers.")
print("You ordered some food from your favorite restaurant and run downstairs with your stomach grumbling.")
print("You open up the resident app (download here) and wait for the locker to open up...")
print("")
#maybe add time here?
print("You find that the locker is empty. You decide to:")

def propertypattifunction():
    print("1. Cry")
    print("2. Look for Property Patti")
    print("3. Look for the carrier who delivered your food")
    answer = input("Enter choice: ")#("Please choose options 1, 2, or 3: ")
    pptime = 0


#answer 1
    if answer == "1":
        print("You cry in a corner: You had a good cry and noticed people staring,\nyou wipe your tears and get back up.")
        print("Time added: 1 minute\n")
        pptime += 1


#answer 2
    elif answer == "2":
        print("Property Patti is new and doesn't recognize you;\nshe asks you for the zip code associated with the location.\nYou answer...")
        question = input("What is the zip code?: ")
        if question == "95652":
            party_list.append("patti")
            print("'Sorry, just had to confirm. Let me take you to the carrier.'")
            print("Property Patti joined your party")


        else:
            print("'Yeah, you don't live here. I can't help you.'")
            print("You wait for the next carrier to arrive")
            print("Time added: 2 minutes")
            inventory.append("wrong_time")
            pptime += 2


#answer 3
    elif answer == "3":
        print("You start looking for the carrier")
        print("You leave the building and start wandering around for a few minutes")
        print("Time added: 3 minutes")
        inventory.append("skipped_time")
        pptime += 3

#anything else
    else:
        print("You stand still wasting time")
        print("Please enter one of the above numbers.")
        print("Time added: 2 minutes")
        print("")
        pptime += 2

    return pptime

#Loop
while "patti" not in party_list and "wrong_time" not in inventory and "skipped_time" not in inventory:
    final_time += propertypattifunction()

#carrier section
print("You approach the carrier")

rand = random.randrange(1,10)
print ("In order for Carl to assist you, you'll need to roll a 3 or higher.\nPress ENTER to roll.")
#Enter roll function here###
if rand >= 3:
    print ("Great, you rolled a ",rand)
    print ("You ask politely and the carrier remembers delivering food to you\nbut also tells you there have been a lot of missing deliveries\nin this area for the last few days.")
    print ("He tells you that the only person who might have information\nabout this is his friend Lisa, Librarian Lisa.\nHe takes you to the library.")
    print ("Carrier Carl joined your party")
    party_list.append("carl")
else:
    print ("Bummer, you rolled a ",rand)
    print ("You yell at the carrier telling him he did a bad job.\nHe apologizes and tells you that he delivered your food into an XL locker at this location by accident.\nHe opens the locker for you and while you are looking, he shoves you in and shuts the door.\nYou notice there is no back and follow a tunnel.")

#End results:
print("Party list: ",party_list)
print ("Inventory: ",inventory)
print ("Final time: ",final_time)


if "carl" in party_list:
    def add_sus_map():
        print("Suspicious Map added to inventory")
        inventory.append('suspicious_map')

    def ll_function():
    
        computer_fix_time = 0
        print("You turn on the computer and open a browser\nYou recieve an error on the Screen\n'no internet'")
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
    
        party_list.append('lisa')
        print("Lisa is so happy you helped her with the computer, she quickly seraches for the map and joins your party.\n")
        computer_fix_time += 3
        print("Librarian Lisa joined your party")
        add_sus_map()
        return computer_fix_time
    
    print("You make your way down to the Library and find Lisa.\nYou ask her for any information she has regarding the missing lockers.\nBeing an expert in her field she knows of a map that might be able to help.\nUnfortunately she is very busy and can't help you look because the computers at the Library are all down.\nYou decide to...\n")
    
    while 'suspicious_map' not in inventory:
        print("1. Search the Location Lisa told you for a map")
        print("2. Help Lisa fix the computer")
        print("3. Go to the coffee shop to get some coffee")
        ll_first_choice = input("Enter Choice: ")
    
        if ll_first_choice == '1' and len(party_list) > 2:
            print("You, Carl, and Patti all search the book section to find a local map, because your party size is 3 you find it quite fast.")
            print("Time added: 5 minutes")
            final_time = final_time + 5
            add_sus_map()
        elif ll_first_choice == '1' and len(party_list) == 2:
            print("You and Carl search the book section and find a local map.")
            print("Time added: 10 minutes")
            final_time = final_time + 10
            add_sus_map()
        elif ll_first_choice == '2':
          print("You have decided to help Lisa troubleshoot the computer.")
          final_time += ll_function()
        elif ll_first_choice == '3' and 'coffee' not in inventory:
          print("You run to the Coffee shop in the library and stand in line for your coffee.\nYou feel refreshed\nCoffee added to inventory")
          print("Time added: 3 minutes")
          final_time = final_time + 3
          inventory.append('coffee')
        elif ll_first_choice == '3' and 'coffee' in inventory:
          print("You already got a coffee\nSelect another option.")
          print("Time added: 1 minute")
          final_time = final_time + 1
        else:
          print("You stand still wasting time")
          print("Please enter one of the above numbers")
          print("Time added: 2 minutes")
          final_time = final_time + 2
    
    print("Now with the map in your possesion\nYou and your party notice a strange line connecting your apartment building to another\nYou follow the line")
    
    print("Party: ", party_list)
    print("Inventory: ", inventory)
    print("Final Time: ", final_time)

def vikki():
    print ("1. Help them with the lockers")
    print ("2. Go ask an associate about the weird tunnel that took you to the store")
    print ("3. Ask a customer that is wandering around.")
    print ("4. Purchase the crowbar you have been meaning to get for home.")
    choice = input("Enter Choice: ")
    vikki_time = 0

    if choice == "1":
        print ("In order to impress Vikki, you'll need to roll a 7  or higher.\nPress ENTER to roll.")
        rand = random.randrange(1,17)
        
        if rand >= 7:
            print("Great, you rolled a", rand)
            print("Vikki is impressed with your assistance and joins the team!")
            party_list.append("vikki")
        else:
            print("Bummer, you rolled a", rand)
        print("You fix the lockers and as you preform the test delivery the package is has dissapeared from the locker.")
        print("You demand a maintence log from the manager with the new found information.")
        inventory.append("maintence_log")
        print(inventory)
        print("Time Added: 15 minutes")
        vikki_time += 15
    

    elif choice == "2":
        if "already_asked" not in inventory:
            print("You find an associate and ask them about the strange tunnel that brought you to the store.")
            rand = random.randrange(1,17)
            print("Roll a 3 or more so the associate understands")
            if rand <= 3:
                print("Great, you rolled a",rand)
                print("'Now that you mention it there has been some strangness with the lockers!' exclaims the associate")
                print("They provide you with the maintence logs to the lockers to help look for clues")
                inventory.append("maintence_log")
                print("Time Added: 10 minutes")
                vikki_time += 10
            else:
                print("Bummer, you rolled a",rand)
                print("'I am sorry but I do not know what you are talking about. I can not let you have this log without proper clearance.'")
                print("Time Added: 5 minutes")
                vikki_time += 5
            inventory.append("already_asked")
        else:
            print("'You already asked me!'")
            print("Time Added: 2 mintues")
            vikki_time += 2

    elif choice == "3":
        print("'Where am I? How did I get here?'")
        print("'This isn't my apartment complex!'")
        print("'There was a carrier'")
        print("'He must have pushed me into the locker!'")
        print("'I found a tunnel and when I crawled through it I was here.'")
        print("Time Added: 5 minutes")
        vikki_time += 5

    elif choice == "4":
        if "crowbar" in inventory:
            print("You already have a crowbar")
            print("Time Added: 2 minutes")
            vikki_time += 2
        else:
            print("You gain a crowbar")
            print("Time Added: 2 minutes")
            vikki_time += 2
            inventory.append("crowbar")
        print(inventory)
    else:
        print ("Enter Choice: ")
    return vikki_time

def postLog():
    print ("1. Alex C.")
    print ("2. Architect Andy")
    print ("3. Install Team")

    choice = input("Enter Choice: ")
    postLog_time = 0

    if choice == "1":
        if "sus" not in inventory:
            print("'Luxer One Retail Support this is Alex'")
            print("You tell him how you are looking for your package, traced it to THD, and found his name in the maintence log")
            print("Alex lets out an audible groan")
            print("'Yeah they are always adding me to these things.'")
            print("'I didn't even need to be there'")
            print("'Andy and I just stood around while installs did their thing'")
            inventory.append("sus")
            print(inventory)
            print("Time Added: 5 minutes")
            postLog_time += 5
        else:
            print("'We just spoke please call anyone else'")
            print("Time Added: 1 minute")
            postLog_time += 1

    elif choice == "2":
        if "locker_location" not in inventory:
            print("'Hello this is Andrew.'")
            print("You tell how you are looking for your package, traced it to THD, and found his name in the maintence log")
            print("'Oh yes of course I was there. Really not an install that can be completed without my assitance.'")
            if "sus" in inventory:
                print ("You tell him how you just got off the phone with Alex and he told you a different story.")
                print ("Andy quickly hangs up on you.")
                print ("You and the party share a concerned look")
                rand = random.randrange(5,17)
            else:
                print ("You call him out about helping with the install.")
                print ("'The gull to say I was not needed for it to be completed. How dare you!'")
                rand = random.randrange(1,17)
            print ("You need to roll 8 or higher")
            if rand >= 8:
                print ("Great, you rolled a",rand)
                print ("The MOD arrives and lets you know they have a video that might be of some use.")
                if "vikki" in party:
                    print("While watching the video Vikki lets you know that is reconizes the store shown and can take you to it.")
                    print("After arriving at the location you notice Andy's car and follow him back to his hideout.")
                    print("Time Added: 30 minutes")
                    postLog_time += 30
                    inventory.append("lockerLocation")
                else:
                    print("You watch the video and it appears to be a different store that you are not familar with")
                    print("You decide to stake out the next install and follow Andy's car back to the hide out.")
                    print("Time Added: 30 minutes")
                    postLog_time += 30
                    inventory.append("lockerLocation")
            else:
                print("Bummer, you rolled a",rand)
                print("You have reached a dead end talking to him.")
                print("Time Added: 2 minutes")
                postLog_time += 2
        else:
            print("*click*")
            print("Time Added: 2 minutes")
            postLog_time += 2

    elif choice == "3":
        print("'Hello Luxer One Installs'")
        print("You tell him how you are looking for your package, traced it to THD, and found his name in the maintence log")
        print("'Ah yes, I remember that install.'")
        print("'Went off without a hitch.'")
        print("'Only strange thing was an Anywhere locker that went missing that day. Nothing about that install though.'")
        if "lisa" in party_list and "failed_locker_roll" not in inventory:
            rand = random(1,17)
            print("You need to roll an 8 or higher")
            if rand <= 8:
                print("Great, you rolled a",rand)
                print("Lisa is able to help you decipher the rep's description of the location where they dropped off the locker.")
                inventory.append("lockerLocation")
            else:
                print("Bummer, you rolled a",rand)
                inventory.append("failed_locker_roll")
                print("Time Added: 1 minute")
                postLog_time += 1
            
        else:
            print("Unable to decipher Install's description of the location you turn to chatbot.")
            print("Chatbot initally responds rather quickly but doesn't understand query.")
            print("After some back and forth they are able to assist and you have the location you seek.")
            inventory.append("lockerLocation")
    else:
        print ("You stand still wasting time")
        print ("Please enter of the above numbers")
        print ("Time Added: 1 minute")
        postLog_time += 1
    return postLog_time

print ("You see an uproar at the lockers and make your way over to them.")
print ("You see Var Vikki and the THD team working on getting the lockers back online.")

while "maintence_log" not in inventory:
    print(inventory)
    final_time += vikki()
    print("Final Time: ", final_time)

print ("You now have the logs of who may have tampered with the locker system and notice that there are three names on the list: ")
while "lockerLocation" not in inventory: 
    print(inventory)
    final_time += postLog()
    print("Final Time: ", final_time)
    
def add_harbor():
    # print('harbor added to inventory')
    inventory.append('harbor')

def carl_bonus():
    if 'Carl' in party_list:
        print('Driving with Carl significantly cuts down on Drive time')
        return 10
    else:
        return 20

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
        
    elif headquarters_choice == '2' and 'patti' in party_list:
        print('Patti is an expert in these lockers\nShe proceeds to open an XL locker...\nYou and your party climb in...\nTime Taken: 1 minute')
        add_harbor()
        break_in_time = 1

    elif headquarters_choice == '2' and 'patti' not in party_list:
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
        print("Please enter one of the above numbers")
        print("Time added: 2 minutes")
        break_in_time = 2

    return break_in_time



if quick_route == 1:
    print('You follow Andy down a long road until you see a lone set of harbor lockers in the middle of nowhere\nYou wait for him to park and enter throug the back of the locker bank.')
else:
    print('You follow the instructions down a long road until you see a lone set of harbor lockers in the middle of nowhere\nYou see a lone truck sitting behind the lockers.')
print('When you get to the locker you dont notice anything that unusual...\nbesides an outfited back that lockes from the inside...\nDo you...')

final_time += carl_bonus()

while 'harbor' not in inventory:
    final_time += headquarters()
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
print('\n\n\n\n\n\n\nTHE END 🎉')
