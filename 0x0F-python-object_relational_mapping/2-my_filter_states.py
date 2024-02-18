#!/usr/bin/python3
"""
a module to match a given argument
with all records in a database
"""

if __name__ == "__main__":
    import sys
    args = sys.argv

    if len(args != 5):
        raise Exception('Kindly enter required arguments')
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=args[1],
                             passwd=args[2], db=args[3])

        cur = db.cursor()
        cur.execute("SET @matchName − = 'args[4]'; SELECT * FROM states WHERE name \
             = @matchName ORDER BY states.id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(e)