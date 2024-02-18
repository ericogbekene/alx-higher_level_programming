#!/usr/bin/python
"""
a module to match a given argument
with all records in a database
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv

    if (len(args) != 5):
        raise Exception('Kindly enter required arguments')
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=args[1],
                             passwd=args[2], db=args[3])

        cur = db.cursor()
        my_query = "SELECT * FROM states WHERE name \
             %s ORDER BY states.id ASC"
        cur.execute(my_query, (args[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()

    except Exception as e:
        print(e)
