from flask_mysqldb import MySQL
from main import mysql

def insertUser(cpf,email,senha):
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO users (cpf,email,senha) VALUES (%s,%s,%s)''', (cpf,email,senha))
    mysql.connection.commit()
    cursor.close()

def retrieveUsers():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT cpf, email FROM users''')
    users = cursor.fetchall()
    cursor.close()
    return users

def retriveLab(labnum):
    cursor = mysql.connection.cursor()
    cursor.execute(f'''SELECT * FROM laboratorio{labnum} ORDER BY pos''')
    computadores = cursor.fetchall()
    cursor.close()
    return computadores