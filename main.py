<<<<<<< HEAD
import time
import random

inventory = []

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
    
=======
print ("1. Find Patti")
print ("2. Cry")
print ("3. Find Carl")

choice = input("Please choose 1,2, or 3: ")
#print ("The choice you made was: " + choice)
:eif choice == "1":
    print("You go find the property manager")
elif choice == "2":
    print ("You cry a little and feel better. There there")
elif choice == "3":
    print ("You look around for the carrier")
else:
    print ("Invalid input please choose 1,2, or 3.")
>>>>>>> Richard
