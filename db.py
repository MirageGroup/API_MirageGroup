from flask_mysqldb import MySQL
from main import mysql
import datetime

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

def makeCall(form, labnum):
    pc_id = form.input_numero_pc.data
    pc_problem = form.pc_problem.data
    problem_description = form.problem_description.data
    labnum = str(labnum)
    cursor = mysql.connection.cursor()
    cursor.execute(f''' INSERT INTO chamados (laboratorio_num, pc_id, data_chamado, hora_chamado, problema_tipo, problema_desc) VALUES (%s, %s, CURDATE(), CURRENT_TIME(), %s, %s) ''', (labnum, pc_id, pc_problem, problem_description))
    mysql.connection.commit()
    cursor.close()