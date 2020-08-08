#!/usr/bin/python3
"""
this script lists all states from db hbtn_0e_0_usa with name starting N
takes 3 arguments mysql username, mysql password, db name
sorted in asc order by states.id
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c_db = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN\
    states ON cities.state_id = states.id"
    c_db.execute(sql)
    query_res = c_db.fetchall()
    for row in query_res:
        print(row)
    c_db.close()
    db.close()
