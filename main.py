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

@app.route('/')
def home():
  return render_template('index.html')

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
  app.run(debug=True)