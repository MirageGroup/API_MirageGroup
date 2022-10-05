import sqlite3 as sql

def insertUser(cpf,email,senha):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (cpf,email,senha) VALUES (?,?,?)", (cpf,email,senha))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT cpf, email FROM users")
	users = cur.fetchall()
	con.close()
	return users