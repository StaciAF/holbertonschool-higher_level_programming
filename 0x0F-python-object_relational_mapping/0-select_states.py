#!/usr/bin/python3
"""
this script lists all states from db hbtn_0e_0_usa
takes 3 arguments mysql username, mysql password, db name
sorted in asc order by states.id
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="127.0.0.1",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c_db = db.cursor()
    sql = "SELECT * FROM `states` ORDER BY `id` ASC"
    c_db.execute(sql)
    query_res = c_db.fetchall()
    for row in query_res:
        print(row)
    c_db.close()
    db.close()
