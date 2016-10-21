import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)", (username,mail,password))
    con.commit()
    con.close()

def retrieveUsers():
    con = sql.connect("db.db")
    cur = con.cursor()
    cur.execute("SELECT username,email, password FROM users")
    users = cur.fetchall()
    con.close()
    return users