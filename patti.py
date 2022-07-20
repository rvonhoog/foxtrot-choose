import time
import random

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
#while "patti" not in party_list and "wrong_time" not in inventory and "skipped_time" not in inventory:
#    final_time += propertypattifunction()

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



