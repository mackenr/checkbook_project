import os
from datetime import date
from datetime import datetime as dt

## Here we ensure that the file is created and in a path that we can read from this point on. It give us headers and an initial line

if os.path.isfile("checkbook.csv") != True:
    with open("checkbook.csv", "w") as f:
        now = dt.now()

        heads = f"Index,Date,Debit/Credit,Debit Credit Amount,Bal\n"
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
        cols = f"{0},{date_time},debit,{0.00},{0.00}\n"
        f.write(heads + cols)


def getbal():
    with open("checkbook.csv", "r") as f:

        currentbal = f.read().split("\n")[-2].split(",")[-1]

    return currentbal


def getIndex():

    """Here we get our index from our record"""
    with open("checkbook.csv", "r") as f:
        currentindex = f.read().split("\n")[-2][0]

        return currentindex


def appendNextline(cols):
    """Here we append new entrys to the record"""
    with open("checkbook.csv", "a") as f:

        f.write(cols)


def showall():
    with open("checkbook.csv", "r") as f:

        all = f.read()
        all

    return all


# %%
def actionFun(action, currentbal):
    action_ammount = float(input(f"Enter {action} amount as xxx.xx format\n"))

    if action == "debit":
        currentbal = currentbal - action_ammount
    else:
        currentbal = currentbal + action_ammount

    now = dt.now()
    index = int(getIndex()) + 1
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
    cols = f"{index},{date_time},{action},{action_ammount},{currentbal}\n"
    appendNextline(cols)

    currentbal = getbal()
    currentbalstring = f"Your current bal is:  {currentbal}\n"

    print(currentbalstring)


def tablemaker(all):
    s = "|"

    for i in all.splitlines():
        karr = []
        for k in i.split(","):
            karr.append(f"{k:<25}")

        karr.append("\n")
        karr = f"{s}".join(karr)
        print(karr)


def checkbookInterface():
    """this is the main program in the base from it allows the user to add a debit or credit and update the balance, also you can check the balace as is."""

    mainprompt = f"""       
        1) view current balance\n
        2) record a debit (withdraw)\n
        3) record a credit (deposit)\n
        4) show all records\n
        5) exit\n

        Your choice?\n 
    """

    quitvar = False

    while quitvar == False:
        currentbal = float(getbal())
        mainuserinput = input(mainprompt)
        invalidstring = f"Invalid choice:{mainuserinput}"
        if mainuserinput == "1":
            currentbalstring = f"Your current bal is:  {currentbal:.2f}\n"
            print(currentbalstring)
        elif mainuserinput == "2":
            action = "debit"
            actionFun(action, currentbal)
        elif mainuserinput == "3":
            action = "credit"
            actionFun(action, currentbal)
        elif mainuserinput == "4":
            all = showall()
            tablemaker(all)

        elif mainuserinput == "5":
            print("Goodbye")
            quitvar = True
        else:
            print(invalidstring)


checkbookInterface()
