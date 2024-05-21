import mysql.connector
from mysql.connector import Error


#------------------------- Creating a Connection with the server -----------------------------------

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        #print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#------------------------------------ Creating a New Database ---------------------------------------

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#------------------------------------ Connecting to the Database ---------------------------------------

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        #print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#--------------------------------- Creating a Query Execution Function ----------------------------------

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#------------------------------------ Creating Tables through python -------------------------------------------------

#I left it all commented because even though you can do it through python, it is not good practice to,
# because you would have to continuously edit the project to add things into the databases.

#create_username_table = """
#CREATE TABLE username (
#  username_id INT PRIMARY KEY,
#  password_id INT NOT NULL,
#  username_name VARCHAR(40) UNIQUE NOT NULL
#  );
# """

#connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
#execute_query(connection, create_username_table) # Execute our defined query


#create_password_table = """
#CREATE TABLE password (
#  password_id INT PRIMARY KEY,
#  username_id INT NOT NULL,
#  password_name VARCHAR(40) NOT NULL
#  );
# """

#connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
#execute_query(connection, create_password_table) # Execute our defined query