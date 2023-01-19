import sqlite3

class Usersdb:
    def __init__(self):
        conn = sqlite3.connect('users_entry.db')
        cur = conn.cursor()

        #Create table 
        cur.execute("""
                CREATE TABLE users
                (FirstName, LastName, CurrSkills, FutureSkills, DayTimeAvail)
                """)

        conn.commit()
        conn.close()



    
