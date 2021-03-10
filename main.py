# imports

import csv
# csv because we are using csv file

import random
# random to decide whether an "user" will get VIP or not

# we are done with imports

"""List And Variables Needed For The File"""
list = ["True", "False"]
fieldnames = ["name", "pin", "amount", "vip", "owner"]

# ask the user where they want to be redirected
ask_User = input("Where Would You Like To Be Redirected? Type CA to create account and AC to Access your Account:\n")

# check what the user said

if ask_User.upper() == "CA" or ask_User.upper() == "CREATE ACCOUNT":
    print("You Have Been Redirected To Register Section\n")

    # Obtain the Name
    Name = input("Enter Your Name:\n")

    # Obtain an unique pin
    Pin = input("\nCreate Your Own Unique Pin:\n")

    if len(str(Pin)) != 4:
        print("Pin Should Be Of 4 Digits")
        exit()

    else:
        pass

    # Pin should be of 4 digits,
    # otherwise anyone can access the "system's" key, its 5 digit

    # We Will Make their Balance 0
    # and Has VIP will be decided randomly

    # Declare the Has VIP variable
    Has_VIP = random.choice(list)

    # open the file, with "with open()" function

    with open("data.csv", "a", newline="") as data:
        writer = csv.DictWriter(data, fieldnames=fieldnames)

    #    writer.header()
    # I Commented Out The Write Header Because
    # Once We Run This File It Will Ruh The Data File it will write the header again and again
    # so Its Better to Write The Header Manually

        writer.writerow({"name": Name, "pin": Pin, "amount": "0000", "vip": Has_VIP, "owner": "False"})

        # we are done with Create Account or CA part
        print("your Account Has Been Created!")

if ask_User.upper() == "AC" or ask_User.upper() == "ACCESS ACCOUNT":

    Name2 = input("Please Enter Your Name:\n")

    Pin2 = input("\nPlease Enter Your Pin:\n")

    if len(str(Pin2)) != 4:
        print("Pin Should Be Of 4 Digits!")
        exit()

    else:
        pass

    with open("data.csv", "r") as data2:
        format = csv.DictReader(data2)

        for line in format:
            Real_Pin = line["pin"]
            Real_Name = line["name"]

            if Real_Pin == Pin2 and Real_Name == Name2:

                print(f"Access Granted! your Name: {line['name']}, Amount: {line['amount']}, Has Vip: {line['vip']}")

            else:
                print("Something Is Not right, Re-check your Values!")


else:
    exit()
                      
                      

                     
                      
# i was having trouble with if and else statements so its just a exit() sign at last, it was malfunction
