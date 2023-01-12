
"""
Author: Trish Tatel
Date: 12/01/22

About:
Example code on app.py where connection to database is established 
"""

#Expected in app.py
"""
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            answers_list = [request.form['FirstName'],
                           request.form['LastName'],
                           request.form['CurrSkills'],
                           request.form['FutureSkills'],
                           request.form['DayTimeAvail'] ]

            conn = get_db_connection()
            conn.executemany("INSERT into users
                        values (?, ?, ?, ?, ?)",
                        answers_list)

            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')
"""

#Must initialise the database in main.py 
#main.py should run both app.py and users_db.py 
