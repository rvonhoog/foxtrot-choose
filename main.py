import time
import random

inventory = []
party_list = []
final_time = 0
quick_route = 0

print ("You wake up to a notification on your phone, your package has arrived at the lockers… you run downstairs with your stomach grumbling.")
print ("You ordered some food from your favorite restaurant.")
print ("You open up the resident app (download here) and wait for the locker to open up... ")
print (" ")

#should include option to open locker so the user can read the text and prompt the locker opening (and time delay) themselves

def first_text():
    print ("The locker is empty. You decide to:")
    print ("1. Cry")
    print ("2. Look for Property Patti.")
    print ("3. Run down the street to catch the courier.")


    d1 = input ()
    if d1 == '1':
        print ("You cry in a corner: You had a good cry and noticed people staring, you wipe your tears and get back up.")
        inventory.append('cry')
        print(inventory)

    elif d1 == "2":
        
        print ("Property Patty is new and doesn’t recognize you; she asks you for the zip code associated with the location. You answer…")
            #this is where the zip code would go, i guess i can just enter filler
        print ("Enter the zip code:")


        d1sq1 = input()
            #d1sq1 = decision 1 sub-question 1

        if d1sq1 != "95835":
            print ("You don't belong here. Property patty then sticks you in a cannon and shoots you out of the building, you then eat shit and die") #placeholder for the data import that needs to be entered

        else:
            print ("You gain a follower in the campaign and she brings you to the next stop in Carrier Carl’s route")
            #need to add Property Patty onto the team here

    elif d1 == "3":
        print ("You are now standing in front of the carrier and decide to ask him about the missing delivery. He is looking very tired and sweaty and worn out from the hot day. (roll for next play)")
        rand = random.randrange(1,17)
        print (rand)
        if rand <= 6:
            print ("You ask politely and the carrier remembers delivering food to you but also tells you there have been a lot of missing deliveries in this area for the last few days.")

        else:
            print ("You yell at the courier telling him he did a bad job. He apologizes and tells you that he delivered your food into an XL locker at this location by accident (Altough you knew it wasn't an accident). He opens the locker for you and while you are looking, he shoves you in and shuts the door. You notice there is no back and follow a tunnel.")
            has_item = 1
    #   print ("Invalid input please choose 1, 2, or 3") #placeholder for invalid input

while 'cry' not in inventory:
    first_text()
    print(inventory)


if "Carl" in party_list:
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
    
def vikki():
    print ("You see an uproar at the lockers and make your way over to them.")
    print ("You see Var Vikki and the THD team working on getting the lockers back online.")
    print ("Do you...")
    print ("1. Help them with the lockers")
    print ("2. Go ask an associate about the weird tunnel that took you to the store")
    print ("3. Ask a customer that is wandering around.")
    print ("4. Purchase the crowbar you have been meaning to get for home.")
    choice = input("Select 1,2,3, or 4: ")

    if choice == "1":
        # addTime()
        rand = random.randrange(1,17)
        print (rand)
        if rand >= 7:
            #addPerson(vikki)
            print("Vikki is impressed with your assistance and joins the team!")
        print("You fix the lockers and as you preform the test delivery the package is has dissapeared from the locker.")
        print("You demand a maintence log from the manager with the new found information.")
        inventory.append(  "maintenceLog")
        print(inventory)
    elif choice == "2":
        print("You find an associate and ask them about the strange tunnel that brought you to the store.")
        rand = random.randrange(1,17)
        print (rand)
        if rand <= 3:
            print("'Now that you mention it there has been some strangness with the lockers!' exclaims the associate")
            print("They provide you with the maintence logs to the lockers to help look for clues")
            inventory.append("maintenceLog")
        else:
            print("'I am sorry but I do not know what you are talking about. I can not let you have this log without proper clearance.'")
    elif choice == "3":
        print("'Where am I? How did I get here?'")
        print("'This isn't my apartment complex!'")
        print("'There was a carrier'")
        print("'He must have pushed me into the locker!'")
        print("'I found a tunnel and when I crawled through it I was here.'")

    elif choice == "4":
        if "crowbar" in inventory:
            print("You already have a crowbar")
        else:
            print("You gain a crowbar")
            inventory.append("crowbar")
        print(inventory)
    else:
        print ("Invalid input please choose 1,2,3, or 4")

def postLog():
    print ("You now have the logs of who may have tampered with the locker system and notice that there are three names on the list: ")
    print ("1. Alex C.")
    print ("2. Architect Andy")
    print ("3. Install Team")

    choice = input("Select 1,2, or 3: ")

    if choice == "1":
        print("'Luxer One Retail Support this is Alex'")
        print("You tell him how you are looking for your package, traced it to THD, and found his name in the maintence log")
        print("Alex lets out an audible groan")
        print("'Yeah they are always adding me to these things.'")
        print("'I didn't even need to be there'")
        print("'Andy and I just stood around while installs did their thing'")
        inventory.append("sus")
        print(inventory)

    elif choice == "2":
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
        if rand >= 8:
            print ("The MOD arrives and lets you know they have a video that might be of some use.")
            if "vikki" in party:
                print("While watching the video Vikki lets you know that is reconizes the store shown and can take you to it.")
                print("After arriving at the location you notice Andy's car and follow him back to his hideout.")
                inventory.append("lockerLocation")
            else:
                print("You watch the video and it appears to be a different store that you are not familar with")
                print("You decide to stake out the next install and follow Andy's car back to the hide out.")
                inventory.append("lockerLocation")

    elif choice == "3":
        print("'Hello Luxer One Installs'")
        print("You tell him how you are looking for your package, traced it to THD, and found his name in the maintence log")
        print("'Ah yes, I remember that install.'")
        print("'Went off without a hitch.'")
        print("'Only strange thing was an Anywhere locker that went missing that day. Nothing about that install though.'")
        if "lisa" in party_list:
            rand = random(1,17)
            if rand <= 8:
                print("Lisa is able to help you decipher the rep's description of the location where they dropped off the locker.")
                inventory.append("lockerLocation")
            else:
                party_list.remove("lisa")
        else:
            print("Unable to decipher Install's description of the location you turn to chatbot.")
            print("Chatbot initally responds rather quickly but doesn't understand query.")
            print("After some back and forth they are able to assist and you have the location you seek.")
            inventory.append("lockerLocation")
    else:
        print ("Invalid input please choose 1,2,3, or 4")

while "maintenceLog" not in inventory:
    print("inventory")
    vikki()

while "lockerLocation" not in inventory: 
    print("inventory")
    postLog()
    
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

from random import randint

#inventory = ['maintenceLog', 'lockerLocation','crowbar']
#party_list = ['Randy', 'asd']
#quick_route = 0
#test = 0
#final_time = 25

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
        print('With the strength of the whole party you are able to aprehend the Suspect\nJust as you thought it was Architect Andy\nHe tels you all about the tunnels he built\nYou saved the day, and everyone found their missing packages.')
        inventory.append('end_game')
    elif aa_choice == '1' and len(party_list) < 5:
        print('Without the strength of the whole party you are not able to aprehend the Suspect\nHe slips away through his tunnels he built under the city...\nYou have not see the last of me, he shouts as his voice fades away.')
        inventory.append('end_game')
    elif aa_choice == '2' and len(party_list) <= 2:
        print('With the small party size you could creep up on the figure\nYou recgonize Architect Andy from his picture\nYou call the authorities and they come and aprehend Andy\nHe shouts about getting revenge\nYou found the missing packages and saved the day')
        inventory.append('end_game')
    elif aa_choice == '2' and len(party_list) > 2:
        print('Your party is too large to sneak up\nHe slips away through his tunnels he built under the city...\nYou have not see the last of me, he shouts as his voice fades away.\nYou found the missing packages and saved the day\nfor now....')
        inventory.append('end_game')
    else:
        print('No time to waste!!')

while 'end_game' not in inventory:
    boss_fight(final_time)


print('\n\n\n\n\n\n\nTHE END 🎉')
