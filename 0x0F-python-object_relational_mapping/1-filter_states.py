#!/usr/bin/python3
""" Sql import using Mysqldb """

if __name__ == '__main__':
    import MySQLdb
    import sys
    
    args = sys.argv

    if (len(args) != 3):
        print('Kindly enter at least 3 arguments')

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=args[0], passwd=args[1], db=args[2])

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name='N' ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            for column in row:
                print('%s\t' % column)
            print ("\n")
            
    except Exception as e:
        print(e)