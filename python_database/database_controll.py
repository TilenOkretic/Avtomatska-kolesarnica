"""Databese working

TODO:
    <+> command LIBRARY
    <->
"""

from user import User
import MySQLdb
import command_lib as lib

###########################SETUP DATABASE#######################################
DB = MySQLdb.connect(host="localhost", user="root", password="user")

CUR = DB.cursor()

ATTRIB = {}
USERS = []

###############################################################################

def log(msg):
    """prints a log message
    Arguments:
        msg {string} -- message
    """
    print msg

def var_char(_x=0):
    """Creats a string version of VARCHAR function
    Arguments:
        x {integer} -- [description]
    Returns:
        string -- [description]
    """
    return "VARCHAR(" + str(_x) + ")"

def db_exists_funcion(db_name=""):
    """Checks if database exists
    Keyword Arguments:
        db_name {str} -- name of the database (default: {""})
    Returns:
        boolean -- result if database exists or not
    """
    result = CUR.execute(lib.show_database_like(db_name))
    if result:
        return True

    return False

def table_exists_funcion(table_name=""):
    """Checks if table exists NOTE: You must be using a database otherwise it wll thorw an error!
    Keyword Arguments:
        table_name {str} -- name of the table (default: {""})
    Returns:
        boolean -- result if table exists or not
    """
    result = CUR.execute(lib.show_table_like(table_name))
    if result:
        return True

    return False

def create_database_function(db_name):
    """Creates a database
    Arguments:
        db_name {string} -- name of the database
    """
    if db_exists_funcion(db_name):
        log("DATABASE: " + db_name + " already exists!")
    else:
        CUR.execute(lib.CREATE_DATABASE + db_name)
        log("Database created: " + db_name)

def drop_database_function(db_name):
    """Destorys the database
    Arguments:
        db_name {string} -- database name
    """
    if db_exists_funcion(db_name):
        CUR.execute(lib.DROP_DATABASE + db_name)
        log("Database destoryed: " + db_name)
    else:
        log("DATABASE: "  + db_name + " does not exist!")

def generate_attributes(attributes):
    """Generates the string with attributes for parameters for creating a table
    Keyword Arguments:
        attributes {dict} -- stores raw attribute data (default: {{}})
    Returns:
        string -- generated a string to insert into create table
    """
    res = ""
    for _x in range(len(attributes)):

        if len(attributes) - _x > 1:
            res += attributes[_x][0] + " " + attributes[_x][1] + ","
        else:
            res += attributes[_x][0] + " " + attributes[_x][1]

    return res

def create_table(db_name, table_name, attributes):
    """Creates a table inside the specified database
    Arguments:
        db_name {string} -- name of the database
        table_name {string} -- name of the table
        attributes {dict} -- a dictionary that contaisn attributes of the table
    """
    if db_exists_funcion(db_name):
        CUR.execute(lib.USE + db_name)
        log("USING: " + db_name)
        CUR.execute(lib.CREATE_TABLE + table_name + "(" + generate_attributes(attributes) + ")")
        log(lib.CREATE_TABLE + table_name + "(" + generate_attributes(attributes) + ")")
    else:
        log("DATABASE: "  + db_name + " does not exist!")

def insert_into_table(db_name, table_name, users_array, attributes):
    """Inserts values into table
    NOTE: This is made only to work with the specific class called USERS,
          if you need to change this function to suit your needs
    Arguments:
        db_name {string} -- name of the database in use
        table_name {string} -- name of the table in use
        users_array {array} -- stores all of the user data
        attributes {array} -- stores all of the atubutes that a table has
    """
    if db_exists_funcion(db_name):
        CUR.execute(lib.USE + db_name)
        log("USING: " + db_name)
        if table_exists_funcion(table_name):
            res = lib.INSERT_INTO + table_name + "("
            for _x in range(len(attributes)):
                if len(attributes) - _x > 1:
                    res += str(attributes[_x][0]) + ","
                else:
                    res += str(attributes[_x][0])

            res += ") values("

            for usr in users_array:
                temp = ""
                i = 0
                for user_data in usr.data:
                    temp += str(user_data)
                    i += 1
                    if i < len(usr.data) - 1:
                        temp += ','

                log(res  + temp + ")")
                CUR.execute(res  + temp + ")")
                DB.commit()
        else:
            log("TABLE: " + table_name + " does not exit!")
    else:
        log("DATABASE: "  + db_name + " does not exist!")

###############################################################################

ATTRIB[0] = ["ime", var_char(20) + " NOT NULL PRIMARY KEY"]
ATTRIB[1] = ["id", "INT" + " NOT NULL"]

###############################################################################

USERS.append(User(["""'Matej'""", ", 030300"]))

###############################################################################

drop_database_function("workers")

create_database_function("workers")

create_table("workers", "worker", ATTRIB)

insert_into_table("workers", "worker", USERS, ATTRIB)

###############################################################################

DB.close()
