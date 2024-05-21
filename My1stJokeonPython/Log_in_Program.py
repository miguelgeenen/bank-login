#-------------------------------- This is for MySQL -------------------------------------------
import DataBase_Related
import Menus

menu = Menus

pw = "AceR1996lol!"  #root password
db = "credentials"  #Database name
connection = DataBase_Related.create_server_connection("localHost", "root", pw)
cursor = connection.cursor()

#------------------------------ Only need these once ---------------------------------
#create_database_query = "CREATE DATABASE credentials”
#create_database(connection, create_database_query)


def main():
    while True:
        username = menu.loginMenu(cursor, connection)

        if username == "Admin":
            menu.adminMenu(cursor, connection)
            continue

        else:
            menu.mainMenu(cursor, connection, username)
            continue


if __name__ == '__main__':
    main()