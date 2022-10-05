<<<<<<< Updated upstream
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
=======

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
>>>>>>> Stashed changes
import models as dbHandler

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10524553'
app.config['MYSQL_PASSWORD'] = 'XWDCjSPxS1'
app.config['MYSQL_DB'] = 'sql10524553'

mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
  if request.method == 'POST':
    cpf=request.form['cpf']
    email=request.form['email']
    senha=request.form['senha']
    dbHandler.insertUser(cpf,email,senha)
    return redirect('/')
  else:
    users = dbHandler.retrieveUsers()
    return render_template('index.html', users=users)

@app.route('/lab/<int:labnum>')
def lab(labnum):
  cursor = mysql.connection.cursor()
  cursor.execute(f'''SELECT * FROM laboratorio{labnum} ORDER BY pos''')
  computadores = cursor.fetchall()
  return render_template('laboratorio.html', labnum=labnum, computadores=computadores)

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  cursor = mysql.connection.cursor()
  cursor.execute(f'''SELECT * FROM laboratorio{labnum} ORDER BY pos''')
  computadores = cursor.fetchall()
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores)

@app.route('/lab_3')
def lab_3():
  return render_template('lab_3.html')

<<<<<<< Updated upstream
=======
@app.route('/lab_edit')
def lab_edit():
  return render_template('laboratorio_editor.html')

@app.route('/tecnico')
def tecnico():
  return render_template('tecnico.html')

>>>>>>> Stashed changes
if __name__ == '__main__':
  app.run(debug=True)#pode ser mudado para 127.0.0.1