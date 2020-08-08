#!/usr/bin/python3
"""
this script lists all states from db hbtn_0e_0_usa with name starting N
takes 3 arguments mysql username, mysql password, db name
sorted in asc order by states.id
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c_db = db.cursor()
    state_srch = (argv[4], )
    c_db.execute("SELECT cities.name FROM cities\
    INNER JOIN states on cities.state_id = states.id\
    WHERE states.name=%s\
    ORDER BY cities.id", state_srch)
    query_res = c_db.fetchall()
    complete_str = []
    for rows in query_res:
        city_str = str(rows).strip("()")
        city_str = city_str.replace("'", '')
        city_str = city_str.replace(",", "")
        complete_str.append(city_str)
    print(', '.join(complete_str))
    c_db.close()
    db.close()
