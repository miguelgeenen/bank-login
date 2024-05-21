from sty import fg

import BalanceLogic
import MyFunctions
import sys
import MenuLogic

myFunctions = MyFunctions
menuLogic = MenuLogic
balanceLogic = BalanceLogic


#########################################################################################################
################################ ------------ LOG IN MENU ------------- #################################
#########################################################################################################

def loginMenu(cursor, connection):
    while True:
        print("""\n########################
########""" + fg.yellow + """ LOG IN """ + fg.rs + """########
########################\n""")

        choice = input("1 -> Log In\n2 -> Create Account\n0 -> Exit Program\n\n-> ")

        if choice == '1':  # Log In

            while True:
                username = input("\nEnter Username:\n-> ")

                if not myFunctions.usernameChecking_login(cursor, username):
                    break

                else:
                    if not myFunctions.passwordChecking_login(cursor, username):
                        break
                    else:
                        print("\nLogged In Successfully.\n\nWellcome " + fg.li_yellow + username + fg.rs + ".\n")
                        return username

        elif choice == '2':  # Create Account
            menuLogic.createAccount(cursor,connection)

        elif choice == '0':  # Exit Program
            print("\n\nExiting now...")
            sys.exit(1)
        else:
            print("\nPlease select one of the given options to proceed.\n\n")


#########################################################################################################
################################# ------------ USER MENU ------------- ##################################
#########################################################################################################

def mainMenu(cursor, connection, username):
    while True:
        print("""\n#########################
#######""" + fg.green + """ MAIN MENU """ + fg.rs + """#######
#########################\n""")

        choice = input("1 -> Profile\n2 -> Check Balance\n3 -> Withdraw\n4 -> Deposit\n5 -> Transfer\n0 -> Log Out\n\n-> ")

        if choice == '1': # Profile
            profileMenu(cursor, connection, username)

        elif choice == '2': # Check Account Balance
            balance = balanceLogic.balanceGetter(cursor, username)
            print(fg.grey + "\nBalance: " + fg.rs + balance + "\n")
            continue

        elif choice == '3': # Withdraw
            balanceLogic.withdraw(cursor, connection, username)
            continue

        elif choice == '4': # Deposit
            balanceLogic.deposit(cursor, connection, username)
            continue

        elif choice == '5': # Transfer
            balanceLogic.transfer(cursor, connection, username)
            continue

        elif choice == '0': # Log Out
            myFunctions.logout()
            break
        else:
            print("\nPlease select one of the given options to proceed.\n")
            continue


#########################################################################################################
############################# ----------- USER PROFILE MENU ------------- ###############################
#########################################################################################################

def profileMenu(cursor, connection, username):
    while True:
        print("""\n##########################
######""" + fg.cyan + """ PROFILE MENU """ + fg.rs + """######
##########################\n""")
        choice = input("1 -> Check Details\n2 -> Alter Data\n3 -> Delete Account\n0 -> Return\n\n-> ")

        if choice == '1': # Check Details
            myFunctions.userDataGetter(cursor, username)
            continue

        elif choice == '2': # Alter Data
            print("\n(" + fg.yellow + "Please remember that in order to complete alteration of Data, the program will Self-Restart" + fg.rs + ")")
            menuLogic.alterAccountData(cursor, connection, username)
            break

        elif choice == '3': # Delete Account
            if not menuLogic.deleteAccount(cursor, connection, username):
                continue
            else:
                break

        elif choice == '0': # Return to previous Menu
            print("\nReturning...\n\n")
            break
        else:
            print("\nPlease select one of the given options to proceed.\n")
            continue


#########################################################################################################
################################# ----------- ADMIN MENU ------------- ##################################
#########################################################################################################

def adminMenu(cursor, connection):
    while True:
        print("""\n##########################
#######""" + fg.green + """ ADMIN MENU """ + fg.rs + """#######
##########################\n""")

        choice = input("1 -> Delete Account\n2 -> Alter Account Data\n3 -> Check Account Details\n0 -> Log Out\n\n-> ")

        if choice == '1': # Delete Selected Account
            accountDeleteUsername = input("\nWrite the Username of the Account you wish to Delete:\n-> ")

            if accountDeleteUsername == 'Admin':
                print("\nCan't delete Admin's account.\n")
                continue
            elif not myFunctions.usernameGetter(cursor, accountDeleteUsername):
                continue
            else:
                accountDeletePassword = input("Enter Password of the User '" + accountDeleteUsername + "':\n-> ")

                if not myFunctions.passwordGetter(cursor, accountDeletePassword, accountDeleteUsername):
                    continue
                else:
                    myFunctions.deleteAccount(cursor, connection, accountDeleteUsername)
                    continue

        elif choice == '2': # Alter Selected Account
            accountChangingUsername = input("\nWrite the Username of the Account that you wish to Alter Data from:\n-> ")

            if accountChangingUsername == 'Admin':
                print("\nCan't alter Admin's account details.\n")
                continue

            if not myFunctions.usernameGetter(cursor, accountChangingUsername):
                continue
            else:
                accountChangingPassword = input("\nEnter Password of the User '" + accountChangingUsername + "':\n-> ")

                if not myFunctions.passwordGetter(cursor, accountChangingPassword, accountChangingUsername):
                    continue
                else:
                    while True:
                        print("\nWhat would you like to Alter in " + accountChangingUsername + "'s Account?\n")
                        choiceAlter = input("1 -> Username\n2 -> Password\n0 -> Return\n\n-> ")

                        if choiceAlter == '1': # Alter Selected Account Username
                            newUsername = input("\nType new Username:\n-> ")

                            if myFunctions.usernameCreation(cursor, newUsername) == 0:
                                continue
                            else:
                                myFunctions.alterAccountUsername(cursor, connection, accountChangingUsername, newUsername)
                                break

                        elif choiceAlter == '2': #Alter Selected Account Password
                            newPassword = input("\nType new Password:\n-> ")

                            if myFunctions.passwordCreation(cursor, newPassword) == 0:
                                continue
                            else:
                                myFunctions.alterAccountPassword(cursor, connection, accountChangingPassword, newPassword)
                                break

                        else:
                            print("\nPlease type one of the given options.\n\n")
                            continue

        elif choice == '3': # Check Selected Account Details
            detailsAdminMenu(cursor)
            continue

        elif choice == '0': # Log Out
            myFunctions.logout()
            break
        else:
            print("Please select one of the given options to proceed.\n\n")


#########################################################################################################
############################# ----------- ADMIN DETAILS MENU ------------- ##############################
#########################################################################################################

def detailsAdminMenu(cursor):
    while True:
        print("""\n################################
######""" + fg.magenta + """ ADMIN DETAILS MENU """ + fg.rs + """######
################################\n""")

        choice = input("1 -> Specific User\n2 -> List All Users\n0 -> Return\n\n-> ")


        if choice == '1':
            user = input("\nType the username of the user to check details from:\n-> ")

            if not myFunctions.usernameGetter(cursor, user):
                break
            else:
                myFunctions.userDataGetter(cursor, user)
            return

        elif choice == '2':
            myFunctions.allDataGetter(cursor)
            return

        elif choice == '0':
            return
