from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from jinja2 import Environment
import json

app = Flask(__name__)

jinja_env = Environment(extensions=['jinja2.ext.i18n'])
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['NYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'api'

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

if __name__ == '__main__':
  app.run(debug=True)#pode ser mudado para 127.0.0.1