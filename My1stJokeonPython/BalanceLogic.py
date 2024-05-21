from sty import fg

import MyFunctions


def balanceGetter(cursor, username): # RETURNS BALANCE OF USER
    statementUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(statementUserID)
    fetchUserID = cursor.fetchone()
    userID = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    statementBalance = "SELECT money FROM credentials.balance WHERE user_id = " + userID + ";"
    cursor.execute(statementBalance)
    fetchBalance = cursor.fetchone()
    balance = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")

    return balance


def withdraw(cursor, connection, username):
    amount = input("\nHow much would you like to Withdraw from your Account?\n-> ")
    amount_int = int(amount)

    statementUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(statementUserID)
    fetchUserID = cursor.fetchone()
    userID = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    accountBalance_statement = "SELECT money FROM credentials.balance WHERE user_id = " + userID + ";"
    cursor.execute(accountBalance_statement)
    fetchBalance = cursor.fetchone()
    balanceInAccount_str = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")
    balanceInAccount_int = int(balanceInAccount_str)


    if balanceInAccount_int < amount_int:
        print("\nWithdrawal was Canceled due to Insufficient Balance.\nReturning...\n")
        return
    else:
        statementAlterBalance = "UPDATE credentials.balance SET money = " + str(balanceInAccount_int - amount_int) + " WHERE user_id = " + userID + ";"
        cursor.execute(statementAlterBalance)
        connection.commit()

        print("\nWithdrawal was a Success.\nReturning...\n")
        return

def simpleWithdraw(cursor, connection, username, amount):
    statementUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(statementUserID)
    fetchUserID = cursor.fetchone()
    userID = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    accountBalance_statement = "SELECT money FROM credentials.balance WHERE user_id = " + userID + ";"
    cursor.execute(accountBalance_statement)
    fetchBalance = cursor.fetchone()
    balanceInAccount_str = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")
    balanceInAccount_int = int(balanceInAccount_str)

    if balanceInAccount_int < amount:
        return 0
    else:
        statementAlterBalance = "UPDATE credentials.balance SET money = " + str(balanceInAccount_int - amount) + " WHERE user_id = " + userID + ";"
        cursor.execute(statementAlterBalance)
        connection.commit()
    return


def deposit(cursor, connection, username):
    amount = input("\nHow much would you like to Deposit into your Account?\n-> ")
    amount_int = int(amount)

    statementUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(statementUserID)
    fetchUserID = cursor.fetchone()
    userID = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    accountBalance_statement = "SELECT money FROM credentials.balance WHERE user_id = " + userID + ";"
    cursor.execute(accountBalance_statement)
    fetchBalance = cursor.fetchone()
    balanceInAccount_str = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")
    balanceInAccount_int = int(balanceInAccount_str)

    statementAlterBalance = "UPDATE credentials.balance SET money = " + str(balanceInAccount_int + amount_int) + " WHERE user_id = " + userID + ";"
    cursor.execute(statementAlterBalance)
    connection.commit()

    print("\nDeposit was a Success.\nReturning...\n")
    return

def simpleDeposit(cursor, connection, username, amount):
    statementUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(statementUserID)
    fetchUserID = cursor.fetchone()
    userID = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    accountBalance_statement = "SELECT money FROM credentials.balance WHERE user_id = " + userID + ";"
    cursor.execute(accountBalance_statement)
    fetchBalance = cursor.fetchone()
    balanceInAccount_str = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")
    balanceInAccount_int = int(balanceInAccount_str)

    statementAlterBalance = "UPDATE credentials.balance SET money = " + str(balanceInAccount_int + amount) + " WHERE user_id = " + userID + ";"
    cursor.execute(statementAlterBalance)
    connection.commit()
    return


def transfer(cursor, connection, username):
    otherUser = input("\nTo who would you like to Transfer to?\n(Type the Username)\n-> ")

    condition = MyFunctions.usernameGetter(cursor, otherUser)

    if condition is False:
        return
    elif condition == username:
        print("\nDont' type your own Username.\n")
        return
    else:
        while True:
            amountTransfer = input("\nHow much would you like to Transfer?\n-> ")

            if amountTransfer.isalpha():
                print("\nPlease don't type Alphabetical characters\n")
                continue
            else:
                special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

                if any(c in special_characters for c in amountTransfer) or " " in amountTransfer:
                    print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
                    continue
                elif amountTransfer == "":
                    print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Username " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
                    continue
                else:

                    choice = input("\nTransfer " + amountTransfer + " to " + otherUser + "? (y/n)\n-> ")

                    if choice == 'n':
                        print("\nCanceling Action.\nReturning...\n\n")
                        break
                    if choice == 'y':

                        if simpleWithdraw(cursor, connection, username, int(amountTransfer)) == 0:
                            print("\nTransfer could not be completed due to the lack of funds of this account.\nReturning...\n\n")
                            break
                        else:
                            simpleDeposit(cursor, connection, otherUser, int(amountTransfer))
                            print("\nTransfer was a success.\n\n")
                            return