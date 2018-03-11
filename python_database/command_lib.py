"""Holds commands
"""
CREATE_DATABASE = "CREATE DATABASE IF NOT EXISTS "
DROP_DATABASE = "DROP DATABASE "

def show_database_like(db_name):
    """Rerurns the command
    Arguments:
        db_name {string} -- [description]
    Returns:
        string -- [description]
    """
    return "SHOW DATABASES LIKE '" + db_name+ "'"

def show_table_like(table_name):
    """Rerurns the command
    Arguments:
        db_name {string} -- [description]
    Returns:
        string -- [description]
    """
    return "SHOW TABLES LIKE '" + table_name+ "'"

CREATE_TABLE = "CREATE TABLE "
USE = "USE "
INSERT_INTO = "INSERT INTO "
