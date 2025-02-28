#name :matt falller
# id: FAL22524952
#last update: 1/1/22
#purpose: give estemates on player salaries and contract lengths

while True:
    noPlayers = input("How many players would you like to assess ")
    try:
        #trys to convert the number of players to an integer
        noPlayers = int(noPlayers)
        if noPlayers >=0:
            break
        else:
            print("This is not a valid number. Enter a valid number")
    except ValueError:
        #if number cant be converted to an integer it asks the user to re input the value
        print("This is not a valid number. Enter a valid number")

#loops the program for as many times as the user inputs
for i in range(noPlayers):
    #validays the age to make sure it is a number
    while True:
        name = input("Enter player's name  ")
        if name.isalpha():
            # checks the value (T/F) of name if false asks user to re enter name
            break
        else:
            print("The player's name is invalid, enter a different name")

    #validates the age is a number and not words
    while True:
        age = input("Player's age ")
        try:
            #trys to convert age to an integer
            age = int(age)
            if age >=0:
                break
            else:
                print("This is not a valid age. Enter a valid age")
        except ValueError:
            #if age cant be converted to an integer it asks the user to re input the value
            print("This is not a valid age. Enter a valid age")

    #ask for player speed
    while True:
        speed = input("Player's speed 0-5 ")
        try:
            # convert to int
            speed = int(speed)
            #checks to see if the speed value isn't bigger than 5 and less than 0
            if speed <= 5 and speed >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            #if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")

    #ask for players shooting
    while True:
        shooting = input("Player's shooting 0-5 ")
        try:
            # convert to int
            shooting = int(shooting)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if shooting <= 5 and shooting >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")


    #ask for players passing
    while True:
        passing = input("Player's passing 0-5 ")
        try:
            # convert to int
            passing = int(passing)
            # checks to see if the passing value isn't bigger than 5 and less than 0
            if passing <= 5 and passing >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")

    #ask for players defending
    while True:
        defending = input("Player's defending 0-5 ")
        try:
            # convert to int
            defending = int(defending)
            # checks to see if the defending value isn't bigger than 5 and less than 0
            if defending <= 5 and defending >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")


    #ask for players dribbling
    while True:
        drib = input("Player's dribbling 0-5 ")
        try:
            # convert to int
            drib = int(drib)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if drib <= 5 and drib >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")


    #ask for players physicality
    while True:
        phy = input("Player's physicality 0-5 ")
        try:
            #convert to int
            phy = int(phy)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if phy <= 5 and phy >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("This is not a valid answer. Please enter a valid number between 0-5 ")
    print()
    print()
    #calculates the player overall
    overall = ((speed + shooting + passing + defending + drib + phy) * (100/30))
    # uses a list to store salary details so it is easily changeable
    salary = [1000, 700, 500, 400]
    # calculates the salary based on the overall
    if overall <= 30:
        print("Salary should be", salary[3])
    elif overall <= 45 and overall > 30:
        print("Salary should be", salary[2], salary[3])
    elif overall <= 60 and overall > 45:
        print("Salary should be", salary[1], salary[2])
    elif overall <= 80 and overall > 60:
        print("Salary should be", salary[0], salary[1])
    elif overall > 80:
        print("Salary should be", salary[0])

    #prints the player's overall
    print(name,"has an overall player rating of",overall)

    #calculates if the player's perfomance is likely to decline over the contract due to aging
    if age >= 30:
        print(name, "is getting old so try a shorter contract")
    else:
        print(name, "is still young so try a longer contract")
    print()


