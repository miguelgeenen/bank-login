import Log_in_Program
import MyFunctions

myFunctions = MyFunctions

def createAccount(cursor, connection):
    print("\nAccount Creation Beginning...\n")

    # ------------------------------------- Username ---------------------------------------
    username = input("\n\nEnter Desired Username:\n-> ")
    creationUsernameID = myFunctions.usernameCreation(cursor, username)

    if creationUsernameID == 0:
        return
    else:
        print("\nUsername is Available.\n")

        # ---------------------------------- Password -----------------------------------------
        password = input("Enter Desired Password:\n-> ")
        creationPasswordID = myFunctions.passwordCreation(cursor, password)

        if creationPasswordID == 0:
            return
        else:
            myFunctions.newAccountDBInsert(cursor, connection, creationUsernameID, creationPasswordID, username, password)

def deleteAccount(cursor, connection, username):
    confirmation = input("\nDelete This Account? (y/n)\n-> ")
    usernameCurrent = myFunctions.usernameGetter(cursor, username)

    if confirmation == 'y':  # Yes
        usernameTyped = input("\nPlease write your Username to confirm Account Deletion:\n-> ")

        if usernameTyped != usernameCurrent:
            print("\nWritten username is Different than yours.\nReturning...\n\n")
            return
        else:
            print("\nAccount Deletion confirmed.\nGoodbye " + usernameCurrent + ".\n\n")
            myFunctions.deleteAccount(cursor, connection, usernameCurrent)
            Log_in_Program.main()

    elif confirmation == 'n':  # No
        print("\nReturning...\n\n")
        return
    else:
        print("\nPlease type one of the given options. (y/n)\n\n")
        return



def alterAccountData(cursor, connection, username):
    while True:
        print("\nWhat would you like to alter in your account?\n")
        choiceAlter = input("1 -> Username\n2 -> Password\n0 -> Return\n\n-> ")

        if choiceAlter == '1':  # Alter Username
            currentUsername = input("\nType the current Username:\n-> ")

            if currentUsername != username:
                print("\nUsernames don't match.\nRetuning...\n")
                break
            else:
                while True:
                    newUser = input("\nType the new Username you wish to have:\n-> ")

                    if currentUsername == newUser:
                        print("\nCan't change Username into the current one.\n")
                        break
                    elif myFunctions.usernameCreation(cursor, newUser) == 0:
                        break

                    change = input("\nChange current Username: '" + currentUsername + "', to: '" + newUser + "'? (y/n)\n-> ")

                    if change == 'y':
                        myFunctions.alterAccountUsername(cursor, connection, username, newUser)
                        break
                    elif change == 'n':
                        print("\nUsername has not been changed.\nReturning...\n\n")
                        break
                    else:
                        print("\nPlease type one the given options. (y/n)\n\n")
                break

        elif choiceAlter == '2':  # Alter Password
            inputPass = input("\nType the current Password:\n-> ")
            currentPassword = myFunctions.passwordSimpleGetter(cursor, username)

            if inputPass != currentPassword:
                print("\nPasswords don't match.\nReturning...\n\n")
                break
            else:
                while True:
                    newPass = input("\nType the New Password you wish to have:\n-> ")
                    if newPass == currentPassword:
                        print("\nCan't change Password into the current one.\n")
                        break
                    elif myFunctions.passwordCreation(cursor, newPass) == 0:
                        break

                    change = input("\nChange current Password: '" + currentPassword + "', to: '" + newPass + "'? (y/n)\n-> ")

                    if change == 'y':
                        myFunctions.alterAccountPassword(cursor, connection, currentPassword, newPass)
                        break
                    elif change == 'n':
                        print("\nPassword has not been changed.\nReturning...\n\n")
                        break
                    else:
                        print("\nPlease type one of the given options. (y/n)\n\n")
                break

        elif choiceAlter == '0':  # Return
            print("\nReturning...\n\n")
            break
        else:
            print("\nPlease type one of the given options.\n")
            continue