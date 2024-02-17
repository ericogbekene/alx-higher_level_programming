#!/usr/bin/python3
""" Sql import using Mysqldb """

if __name__ == '__main__':
    import MySQLdb
    import sys
    
    args = sys.argv

    if (len(args) != 4):
        print('Kindly enter at least 3 arguments')

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=args[1], passwd=args[2], db=args[3])

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print (row)
            
    except Exception as e:
        print(e)