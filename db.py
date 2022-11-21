from flask_mysqldb import MySQL
from main import mysql
from main import Session
#import win32com.client as win32

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

def retrieveLab(labnum): 
    cursor = mysql.connection.cursor()
    cursor.execute(f'''SELECT * FROM laboratorio{labnum} ORDER BY pos''')
    computadores = cursor.fetchall()
    cursor.close()
    return computadores

def retrieveCalls(estado):
    cursor = mysql.connection.cursor()
    cursor.execute(f''' SELECT * FROM chamados where estado = '{estado}' ORDER BY data_chamado DESC, hora_chamado DESC ''')
    chamados = cursor.fetchall()
    cursor.close()
    return chamados

    # NUMERO DE CHAMADOS
def retrieveNumbersofCalls():
    cursor = mysql.connection.cursor()
    cursor.execute(f''' SELECT id FROM chamados''')
    numberOfCalls = cursor.fetchall()
    numberOfCalls = len(numberOfCalls)
    return numberOfCalls

    # NUMERO DE CHAMADOS ABERTOS E FECHADOS
def retrieveNumbersOpenOrClose(state):
    
    cursor = mysql.connection.cursor()
    cursor.execute(f''' SELECT id FROM chamados WHERE estado = '{state}' ''')
    numberOfCalls = cursor.fetchall()
    numberOfCalls = len(numberOfCalls)
    return numberOfCalls
    
    # NUMERO DE CHAMADOS POR SALA
def retrieveNumberInLabs(number):
    cursor = mysql.connection.cursor()
    cursor.execute(f''' SELECT id FROM chamados WHERE laboratorio_num = '{number}' ''')
    numberOfCalls = cursor.fetchall()
    numberOfCalls = len(numberOfCalls)
    return numberOfCalls
    
#    NUMERO DE PROBLEMAS ESPECIFICOS
def numberOfProblems(problem):
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT id FROM chamados WHERE problema_tipo = '{problem}' ''')
        numberOfProblems = cursor.fetchall()
        numberOfProblems = len(numberOfProblems)
        return numberOfProblems

def createCall(form, labnum):
    cursor = mysql.connection.cursor()
    pc_id = form.input_numero_pc.data 
    email = form.email.data
    pc_problem = form.pc_problem.data
    problem_description = form.problem_description.data
    labnum = str(labnum)
    email = email + "@fatec.sp.gov.br"
    updatePcStatus(labnum, pc_id, pc_problem, problem_description)
    cursor.execute(f''' INSERT INTO chamados (laboratorio_num, pc_id, data_chamado, hora_chamado, autor, problema_tipo, problema_desc, estado) VALUES (%s, %s, CURDATE(), CURRENT_TIME(), %s, %s, %s, %s) ''', (labnum, pc_id, email, pc_problem, problem_description, 'aberto'))
    mysql.connection.commit()
    cursor.close()

def finishCall(callnumber):
    cursor = mysql.connection.cursor()
    callnumber = str(callnumber)
    cursor.execute(f''' SELECT * FROM chamados WHERE id = {callnumber} ''')
    chamado = cursor.fetchall()
    cursor.execute(f''' UPDATE chamados SET estado = 'fechado' WHERE id = {callnumber} ''')
    mysql.connection.commit()
    pc_description = "O computador está funcionando corretamente"
    pc_id = chamado[0][2]
    cursor.execute(f''' UPDATE laboratorio{chamado[0][1]} SET pc_problema = NULL, pc_descricao = %s WHERE pc_id = %s ''', (pc_description, pc_id))
    mysql.connection.commit()
    cursor.close()
    #enviarEmail(chamado[0][5])

def deleteCall(callnumber):
    cursor = mysql.connection.cursor()
    callnumber = str(callnumber)
    cursor.execute(f''' SELECT * FROM chamados WHERE id = {callnumber} ''')
    chamado = cursor.fetchall()
    cursor.execute(f''' DELETE FROM chamados WHERE id = {callnumber} ''')
    mysql.connection.commit()
    cursor.close()

def updatePcStatus(labnum, pc_id, pc_problem, problem_description):
    cursor = mysql.connection.cursor()
    cursor.execute(f''' UPDATE laboratorio{labnum} SET pc_problema = %s, pc_descricao = %s WHERE pc_id = %s''', (pc_problem, problem_description, pc_id))
    mysql.connection.commit()
    cursor.close()

def retrieveAccessCode():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT acesso FROM acesso_tecnico ''')
    acesso = cursor.fetchall()
    return acesso

def retrieveComponents(labNum):
     cursor = mysql.connection.cursor()
     cursor.execute(f''' SELECT * FROM componentes WHERE laboratorio = {labNum} ''')
     componentes = cursor.fetchall()
     cursor.close()
     return componentes

def updateComponent(componente, labnum, config):
    cursor = mysql.connection.cursor()
    cursor.execute(f''' UPDATE componentes SET {config} = %s WHERE laboratorio = %s ''', (componente, labnum))
    mysql.connection.commit()
    cursor.close()


def saveLayoutPositions(layout_novo, labnum):
    cursor = mysql.connection.cursor()
    lista_posicoes = []
    for i in range(1, 89):
      lista_posicoes.append(i)
    cont = 0
    for i in lista_posicoes:
        cursor.execute(f''' UPDATE laboratorio{labnum} SET pos = %s WHERE pc_id = %s ''', (i, layout_novo[cont]))
        mysql.connection.commit()
        cont += 1
    cursor.close()
    
def addNewPcs(pc_novos_id, pc_novos_pos, labnum):
    cursor = mysql.connection.cursor()
    for i in range(len(pc_novos_id)):
        cursor.execute(f''' INSERT INTO laboratorio{labnum} (pos, pc_id) VALUES (%s, %s) ''', (int(pc_novos_pos[i]), pc_novos_id[i]))
        mysql.connection.commit()
    cursor.close()

def removePcs(remover_pcs_ids, labnum):
  cursor = mysql.connection.cursor()
  for i in remover_pcs_ids:
    cursor.execute(f''' DELETE FROM laboratorio{labnum} WHERE pc_id = %s ''', (i,))
    mysql.connection.commit()
  cursor.close()

def addComentario(comentario, callnumber):
    cursor = mysql.connection.cursor()
    cursor.execute(f''' UPDATE chamados SET comentarios = '{comentario}' WHERE id = '{callnumber}' ''')
    mysql.connection.commit()
    cursor.close()

#def enviarEmail(Email):
    #outlook = win32.Dispatch("outlook.application")
    #email = outlook.CreateItem(0)
    #email.To = f"{Email}"
    #email.Subject = "Chamado Finalizado"
    #email.HTMLBody = f'''
    #<p>Olá</p>
    #<p>Seu chamado realizado no SOS FATEC foi finalizado!</p>

    #<p>confira se o problema foi resolvido! Caso não tenha sido, volte e reporte novamente.</p>
    
    #'''
    #email.Send()
