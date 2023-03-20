##This code can create a .db file
##From https://www.sqlitetutorial.net/sqlite-python/creating-database/ (last accessed 21/09/2021)


import sqlite3


def create_connection(db_file):
    #attempts to create a connection to a SQLite database
    con = None
    try:
        con = sqlite3.connect(db_file)
        print(sqlite3.version)
    except:
        print("Error")
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    ##Note the r before the filepath, there will be a unicode error if it is removed
    create_connection(r"GameData.db")
