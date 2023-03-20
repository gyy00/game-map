##This file contains code that fetches data from the database using SQL
##and includes connecting/closing a database

import sqlite3


#connect to a database
def connectData(dbFile):
    con = sqlite3.connect(dbFile)
    return con

#close database connection
def closeData(con):
    con.close()


def getImage(cur, name, table):
    if (table == 'Locations'):
        cur.execute('SELECT [Image Path] FROM Locations WHERE Name = ?;', (name,))
        path = cur.fetchone()[0]
        return path
    elif (table == 'Unicorns'):
        cur.execute('SELECT [Image Path] FROM Unicorns WHERE Name = ?;', (name,))
        path = cur.fetchone()[0]
        return path
    elif (table == 'Drops'):
        cur.execute('SELECT [Image Path] FROM Drops WHERE Name = ?;', (name,))
        path = cur.fetchone()[0]
        return path

#Locations only
def getBG(cur, name):
    cur.execute('SELECT [BG Path] FROM Locations WHERE Name = ?;', (name,))
    path = cur.fetchone()[0]
    return path

      
#offset is from the top left corner of the image
def getOffset(cur, name):
    cur.execute('SELECT [X Offset], [Y Offset] FROM Locations WHERE Name = ?;', (name,))
    offset = cur.fetchone()
    return offset


#get image dimensions from database
def getLengths(cur, name):
    cur.execute('SELECT [X Length], [Y Length] FROM Locations WHERE Name = ?;', (name,))
    dimensions = cur.fetchone()
    return dimensions
    
