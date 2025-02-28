#name :matt falller
# id: FAL22524952
#last update: 1/1/22
#purpose: give estemates on player salaries and prints their details
import re
from datetime import date
from tabulate import tabulate
#creating lists to later append and store the values into
today = date.today()
overallList = []
salaryList = []
IdList = []
NameList = []
DobList = []
AgeList = []


def main():
    #ask for player speed
    while True:
        global speed
        speed = input("Player's speed 0-5 ")
        try:
            # convert to int
            speed = int(speed)
            #checks to see if the speed value isn't bigger than 5 and less than 0
            if speed <= 5 and speed >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            #if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")

    #ask for players shooting
    while True:
        global shooting
        shooting = input("Player's shooting 0-5 ")
        try:
            # convert to int
            shooting = int(shooting)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if shooting <= 5 and shooting >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")


    #ask for players passing
    while True:
        global passing
        passing = input("Player's passing 0-5 ")
        try:
            # convert to int
            passing = int(passing)
            # checks to see if the passing value isn't bigger than 5 and less than 0
            if passing <= 5 and passing >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")

    #ask for players defending
    while True:
        global defending
        defending = input("Player's defending 0-5 ")
        try:
            # convert to int
            defending = int(defending)
            # checks to see if the defending value isn't bigger than 5 and less than 0
            if defending <= 5 and defending >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")


    #ask for players dribbling
    while True:
        global drib
        drib = input("Player's dribbling 0-5 ")
        try:
            # convert to int
            drib = int(drib)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if drib <= 5 and drib >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")


    #ask for players physicality
    while True:
        global phy
        phy = input("Player's physicality 0-5 ")
        try:
            #convert to int
            phy = int(phy)
            # checks to see if the shooting value isn't bigger than 5 and less than 0
            if phy <= 5 and phy >= 0:
                break
            else:
                # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
        except ValueError:
            # if the values aren't acceptable the user is asked to re input them
                print("The rating you entered was invalid.")
    print()

def calculate_rating():
    #calculates the player overall
    global overall
    overall = ((speed + shooting + passing + defending + drib + phy) * (100/30))
    overallList.append(overall)

def calculate_salary():
    # uses a list to store salary details so it is easily changeable
    salary = [" 1000" , " 700" , " 500" , " 400"]
    playerSalary = 0
    noCom = 0
    # calculates the salary based on the overall
    if overall <= 30:
        playerSalary = (salary[3])
        noCom = playerSalary

    elif overall < 45 and overall > 30:
        playerSalary = (salary[2] + salary[3])
        noBrack = playerSalary.strip("()")
        noCom = re.sub(r"[,]", '', noBrack)
    elif overall == 45:
        playerSalary = (salary[2])
        noCom = playerSalary

    elif overall < 60 and overall > 45:
        playerSalary = (salary[1] + salary[2])
        noBrack = playerSalary.strip("()")
        noCom = re.sub(r"[,]", '', noBrack)

    elif overall == 60:
        playerSalary = (salary[1])
        noCom = playerSalary

    elif overall < 80 and overall > 60:
        playerSalary = (salary[0] + salary[1])
        noBrack = playerSalary.strip("()")
        noCom = re.sub(r"[,]", '', noBrack)

    elif overall >= 80:
        playerSalary = (salary[0])
        noCom = playerSalary

    salaryList.append(noCom)

def playerID():
    while True:
        global PlayerID
        PlayerID = input("Enter player ID ")
        if PlayerID == "end":
            break
        # trys to convert the number of players to an integer
        if len(PlayerID) == 2:
            try:
                PlayerID = int(PlayerID)
                IdList.append(PlayerID)
                break
            except ValueError:
             # if number cant be converted to an integer it asks the user to re input the value
                print("The ID you entered was invalid.")
        else:
            print("The ID you entered was invalid.")

def playerName():
  #  while True:
    name = input("Enter player's name  ")
   #     if name.replace(" ", "").isalpha():
    NameList.append(name)

def ageCheck():
    while True:
        userDOB = input("Enter your DOB")
        try:
            year, month, day = map(int, userDOB.split("-"))
            date1 = date(year, month, day)
            DobList.append(date1)
            age = today.year - year
            AgeList.append(age)
            break
        except ValueError:
            print("The date you entered was invalid.")

PlayerID = ""
#loops the program for 3 many times
for i in range(3):
    playerID()
    if PlayerID == "end":
        break
    playerName()
    ageCheck()
    main()
    calculate_rating()
    calculate_salary()

if len(IdList) == 1:
    # creating a list to store all the infomation gained from the user inputs
    table1 = [["UID", "Name", "D.o.B", "Age", "Score", "Salary Range"],
         [IdList[0],NameList[0],DobList[0],AgeList[0],overallList[0],salaryList[0]]]
    # put all the infomation in the main list into a table
    tableNew = tabulate(table1, headers="firstrow")
    print(tableNew)
elif len(IdList) == 2:
    # creating a list to store all the infomation gained from the user inputs
    table2 = [["UID", "Name", "D.o.B", "Age", "Score", "Salary Range"],
              [IdList[0], NameList[0], DobList[0], AgeList[0], overallList[0], salaryList[0]],
              [IdList[1], NameList[1], DobList[1], AgeList[1], overallList[1], salaryList[1]]]
    # put all the infomation in the main list into a table
    tableNew = tabulate(table2, headers="firstrow")
    print(tableNew)
else:
    #creating a list to store all the infomation gained from the user inputs
    table3 = [["UID", "Name", "D.o.B", "Age", "Score", "Salary Range"],
         [IdList[0],NameList[0],DobList[0],AgeList[0],overallList[0],salaryList[0]],
         [IdList[1],NameList[1],DobList[1],AgeList[1],overallList[1],salaryList[1]],
         [IdList[2],NameList[2],DobList[2],AgeList[2],overallList[2],salaryList[2]]]
    # put all the infomation in the main list into a table
    tableNew = tabulate(table3, headers="firstrow")
    print(tableNew)

# #writes the contents of the table into a text file and then closes that file after its done writing to it
filePlayer = open("players.txt", "w")
filePlayer.write(tableNew)
filePlayer.close()









