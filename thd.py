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
        print("1")
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
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
