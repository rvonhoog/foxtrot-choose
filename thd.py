import random
party = []
inventory = []
hasLog = 0
hasItem = 0

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
        if "lisa" in party:
            rand = random(1,17)
            if rand <= 8:
                print("Lisa is able to help you decipher the rep's description of the location where they dropped off the locker.")
                inventory.append("lockerLocation")
            else:
                party.remove("lisa")
        else:
            print("Unable to decipher Install's description of the location you turn to chatbot.")
            print("Chatbot initally responds rather quickly but doesn't understand query.")
            print("After some back and forth they are able to assist and you have the location you seek.")
            inventory.append("lockerLocation")
    else:
        print ("Invalid input please choose 1,2,3, or 4")

while hasLog != 1:
    print(hasLog)
    vikki()
    if "maintenceLog" in inventory:
        hasLog = 1
    else:
        hasLog = 0

while hasItem != 1:
    print(hasItem)
    postLog()
    if "lockerLocation" in inventory:
        hasItem = 1
    else:
        hasItem = 0
