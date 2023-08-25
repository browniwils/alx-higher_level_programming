#!/usr/bin/python3
"""
Program lists all cities from database
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    host = "localhost" 
    passcode = args[2]
    user = args[1]
    database = args[3]
    port = 3306

    db = MySQLdb.connect(host=host,
                         port=port, passwd=passcode,
                         db=database, user=user)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id""")
    row_data = cursor.fetchall()
    for data in row_data:
        print(data)
    cursor.close()
    db.close()
