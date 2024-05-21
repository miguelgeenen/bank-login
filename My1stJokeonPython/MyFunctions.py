from sty import fg

import DataBase_Related
import Log_in_Program


def checkAndQuery(check, pw, db): # CHECKS CONNECTION WITH DB AND QUERY'S
    connection = DataBase_Related.create_db_connection("localhost", "root", pw, db)  # Connect to the Database
    DataBase_Related.execute_query(connection, check)  # Execute our defined query
    return check

def logout(): # SIMPLE LOG OUT
    print("Logging Session Out.\nReturning...\n")

# -----------------------------------------------------------------------------------------------------
# -------------------------------- Log In Verification Section ----------------------------------------
# -----------------------------------------------------------------------------------------------------

def usernameChecking_login(cursor, username): # USERNAME VERIFICATION FOR LOGIN
    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

    if any(c in special_characters for c in username) or " " in username:
        print(
            "\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return False

    elif username == "":
        print(
            "\nPlease " + fg.red + "don't" + fg.rs + " leave the Username " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return False

    checkUsername_str = "SELECT username_name FROM credentials.username WHERE username_name LIKE '" + username + "';"

    cursor.execute(checkUsername_str)
    checkUsername = cursor.fetchone()

    if checkUsername is None:
        print("\nUsername does not exist\nReturning...\n\n")
        return False
    else:
        return True


def passwordChecking_login(cursor, username): # PASSWORD VERIFICATION FOR LOGIN
    checkUsernameID_str = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"

    cursor.execute(checkUsernameID_str)
    checkUsernameID = cursor.fetchone()

    user_ID_into_str_1 = str(checkUsernameID)
    user_ID_into_str_final = user_ID_into_str_1.replace("(", "").rstrip(",)")

    password = input("\nEnter Password:\n-> ")

    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

    if any(c in special_characters for c in password) or " " in password:
        print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return False

    elif password == "":
        print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Password " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return False

    checkPassword_str = "SELECT password_name FROM credentials.password WHERE password_id = " + user_ID_into_str_final + ";"

    cursor.execute(checkPassword_str)
    checkPassword = cursor.fetchone()

    checkPassword_into_str = str(checkPassword)
    checkPassword_final = checkPassword_into_str.replace("(", "").rstrip(",)").replace("'", "")

    if password == checkPassword_final:
        return True

    else:
        print("\nUsername and Password don't match.\nReturning...\n\n")
        return False


# -----------------------------------------------------------------------------------------------------
# -------------------------------- Account Creation Section -------------------------------------------
# -----------------------------------------------------------------------------------------------------

def usernameCreation(cursor, username): # VERIFIES IF IT'S POSSIBLE TO CREATE WRITTEN USERNAME FOR THE ACCOUNT.
    checkUsername_validity = "SELECT username_name FROM credentials.username WHERE username_name = '" + username + "';"

    cursor.execute(checkUsername_validity)
    usernameValidity = cursor.fetchone()

    usernameValidity_into_str = str(usernameValidity).replace("(", "").rstrip(",)").replace("'", "")

    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

    if any(c in special_characters for c in username):
        print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return 0

    elif username == usernameValidity_into_str:
        print("\nUsername already exists.\n\nReturning...\n\n")
        return 0

    elif username == "":
        print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Username " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return 0

    elif username != usernameValidity_into_str:
        get_last_username_id = "SELECT @last_id := MAX(username_id) FROM credentials.username;"
        cursor.execute(get_last_username_id)
        lastUsernameID = cursor.fetchone()

        lastUsernameID_into_str = str(lastUsernameID).replace("(", "").rstrip(",)").replace("'", "")
        lastUserIDAdd = int(lastUsernameID_into_str) + 1

        creationUsernameID = lastUserIDAdd
        return creationUsernameID


def passwordCreation(cursor, password): # VERIFIES IF IT'S POSSIBLE TO CREATE WRITTEN PASSWORD FOR THE ACCOUNT.
    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨" + ""

    if any(c in special_characters for c in password):
        print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return 0

    elif password == "":
        print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Password " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return 0

    else:
        get_last_password_id = "SELECT @last_id := MAX(password_id) FROM credentials.password;"
        cursor.execute(get_last_password_id)
        lastPasswordID = cursor.fetchone()

        lastPasswordID_into_str = str(lastPasswordID).replace("(", "").rstrip(",)").replace("'", "")
        lastPassIDAdd = int(lastPasswordID_into_str) + 1

        creationPasswordID = lastPassIDAdd
        return creationPasswordID


# -----------------------------------------------------------------------------------------------------
# ------------------------------------------ Data Getters ---------------------------------------------
# -----------------------------------------------------------------------------------------------------

def usernameGetter(cursor, username): # RETURNS USERNAME OF USER
    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

    if any(c in special_characters for c in username) or " " in username:
        print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return False

    elif username == "":
        print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Username " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return False

    checkUsername_str = "SELECT username_name FROM credentials.username WHERE username_name LIKE '" + username + "';"

    cursor.execute(checkUsername_str)
    checkUsername = cursor.fetchone()
    usernameIntoStr = str(checkUsername).replace("(", "").rstrip(",)").replace("'", "")

    if checkUsername is None:
        print("\nUsername does not exist\nReturning...\n\n")
        return False
    else:
        return usernameIntoStr


def passwordGetter(cursor, password, username): # RETURNS PASSWORD OF SELECTED USER
    checkUsernameID_str = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"

    cursor.execute(checkUsernameID_str)
    checkUsernameID = cursor.fetchone()

    user_ID_into_str_1 = str(checkUsernameID)
    user_ID_into_str_final = user_ID_into_str_1.replace("(", "").rstrip(",)")

    special_characters = " " + "!'@#$%^&*()-+?_=,<>/|´`^~ªº£§€{}[];:«»ç\¨"

    if any(c in special_characters for c in password) or " " in password:
        print("\nPlease " + fg.red + "don't" + fg.rs + " use any type of " + fg.li_blue + "Special Characters" + fg.rs + ".\nReturning...\n\n")
        return False

    elif password == "":
        print("\nPlease " + fg.red + "don't" + fg.rs + " leave the Password " + fg.li_blue + "Empty" + fg.rs + ".\nReturning...\n\n")
        return False

    checkPassword_str = "SELECT password_name FROM credentials.password WHERE password_id = " + user_ID_into_str_final + ";"

    cursor.execute(checkPassword_str)
    checkPassword = cursor.fetchone()

    checkPassword_into_str = str(checkPassword)
    checkPassword_final = checkPassword_into_str.replace("(", "").rstrip(",)").replace("'", "")

    if password == checkPassword_final:
        return checkPassword_final

    else:
        print("Username and Password don't match.\nReturning...\n\n")
        return False


def passwordSimpleGetter(cursor, username): # RETURNS PASSWORD OF USER
    checkUsernameID_str = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"

    cursor.execute(checkUsernameID_str)
    checkUsernameID = cursor.fetchone()

    user_ID_into_str_1 = str(checkUsernameID)
    user_ID_into_str_final = user_ID_into_str_1.replace("(", "").rstrip(",)")

    checkPassword_str = "SELECT password_name FROM credentials.password WHERE password_id LIKE '" + user_ID_into_str_final + "';"

    cursor.execute(checkPassword_str)
    checkPassword = cursor.fetchone()

    checkPassword_into_str = str(checkPassword)
    checkPassword_final = checkPassword_into_str.replace("(", "").rstrip(",)").replace("'", "")

    if checkPassword_final is None:
        return
    else:
        return checkPassword_final

def allDataGetter(cursor): # DISPLAYS THE DAT OF ALL USERS IN DB
    statement = "SELECT @last_id := MAX(username_id) FROM credentials.username;"
    cursor.execute(statement)
    lastUserID = cursor.fetchone()

    statement_str = str(lastUserID).replace("(", "").rstrip(",)").replace("'", "")
    statement_int = int(statement_str)
    increment = 0

    while increment <= statement_int:
        usernameStat = "SELECT username_name FROM credentials.username WHERE username_id = " + str(increment) + ";"
        cursor.execute(usernameStat)
        lastUserStat = cursor.fetchone()
        lastUserStat_str = str(lastUserStat).replace("(", "").rstrip(",)").replace("'", "")

        passwordStat = "SELECT password_name FROM credentials.password WHERE password_id = " + str(increment) + ";"
        cursor.execute(passwordStat)
        lastPassStat = cursor.fetchone()
        lastPassStat_str = str(lastPassStat).replace("(", "").rstrip(",)").replace("'", "")

        print(fg.grey + "\nUsername: " + fg.rs + lastUserStat_str + fg.red + " /" + fg.rs + fg.grey + " Password: " + fg.rs + lastPassStat_str)
        increment += 1
    return

def userDataGetter(cursor, username): # DISPLAYS DATA OF USER
    getUserID = "SELECT username_id FROM credentials.username WHERE username_name = '" + username + "';"
    cursor.execute(getUserID)
    fetchUserID = cursor.fetchone()
    UserID_str = str(fetchUserID).replace("(", "").rstrip(",)").replace("'", "")

    getPass = "SELECT password_name FROM credentials.password WHERE password_id = " + UserID_str + ";"
    cursor.execute(getPass)
    fetchPass = cursor.fetchone()
    pass_str = str(fetchPass).replace("(", "").rstrip(",)").replace("'", "")

    getBalance = "SELECT money FROM credentials.balance WHERE user_id = " + UserID_str + ";"
    cursor.execute(getBalance)
    fetchBalance = cursor.fetchone()
    balance_str = str(fetchBalance).replace("(", "").rstrip(",)").replace("'", "")

    print(fg.grey + "\nUsername: " + fg.rs + username + fg.red + " /" + fg.rs + fg.grey + " Password: " + fg.rs + pass_str + fg.red + " /" + fg.rs + fg.grey + " Balance: " + fg.rs + balance_str + "\n")
    return


# -----------------------------------------------------------------------------------------------------
# --------------------------------------Data Insertion on DB-------------------------------------------
# -----------------------------------------------------------------------------------------------------


def newAccountDBInsert(cursor, connection, userID, passID, username, password): # INSERTS DATA OF THE NEWLY CREATED ACCOUNTS INTO DB
    insert_username_to_table = ("""
        INSERT INTO credentials.username (username_id, password, username_name) VALUES
        (""" + str(userID) + """, """ + str(passID) + """, '""" + username + """');""")
    cursor.execute(insert_username_to_table)

    insert_password_to_table = """
        INSERT INTO credentials.password (password_id, username, password_name) VALUES
        (""" + str(passID) + """, """ + str(userID) + """, '""" + password + """');"""
    cursor.execute(insert_password_to_table)

    insert_balance_to_account = "INSERT INTO credentials.balance (user_id, money) VALUES (" + str(userID) + ", 250);"
    cursor.execute(insert_balance_to_account)

    connection.commit()  # Sends data to Database

    print("\nAccount Created Successfully.\nReturning to main menu now...\n\n")


# -----------------------------------------------------------------------------------------------------
# ----------------------------------------- Data Delete -----------------------------------------------
# -----------------------------------------------------------------------------------------------------

def deleteAccount(cursor, connection, username):
    password_id = """SELECT password FROM credentials.username WHERE username_name = '""" + username + """';"""
    cursor.execute(password_id)
    password = cursor.fetchone()

    passwordID_str = str(password).replace("(", "").rstrip(",)").replace("'", "")

    delete_username = """DELETE FROM credentials.username WHERE username_name = '""" + username + """';"""
    cursor.execute(delete_username)

    delete_password = """ DELETE FROM credentials.password WHERE password_id = """ + passwordID_str + """;"""
    cursor.execute(delete_password)

    connection.commit()
    print("The operation has been completed.\nUser '" + username + "' has been deleted.\nReturning...\n\n")

    return

# -----------------------------------------------------------------------------------------------------
# ----------------------------------------- Data Changing ---------------------------------------------
# -----------------------------------------------------------------------------------------------------

def alterAccountUsername(cursor, connection, username, newUsername):
    statement = "UPDATE credentials.username SET username_name = '" + newUsername + "' WHERE username_name = '" + username + "';"
    cursor.execute(statement)
    connection.commit()
    print("Username altered successfully.\n\n")
    Log_in_Program.main()

def alterAccountPassword(cursor, connection, password, newPassword):
    statement = "UPDATE credentials.password SET password_name = '" + newPassword + "' WHERE password_name = '" + password + "';"
    cursor.execute(statement)
    connection.commit()
    print("Password altered successfully.")
    return
