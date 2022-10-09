from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import db as dbHandler
from models.forms import callForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MirageGroup'

app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'bbc6f0cc739a84'
app.config['MYSQL_PASSWORD'] = '2c05d7ed'
app.config['MYSQL_DB'] = 'heroku_be80b7ca2ec9c96'

mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
  if request.method == 'POST':
    CPF = request.form['cpf']
    email = request.form['email']
    senha = request.form['senha']
    dbHandler.insertUser(CPF,email,senha)
    return redirect('/')
  else:
    users = dbHandler.retrieveUsers()
    return render_template('index.html', users=users)

@app.route('/lab/<int:labnum>', methods = ['POST', 'GET'])
def lab(labnum):
  if request.method == 'POST':
    form = callForm()
    if form.validate_on_submit():
      dbHandler.makeCall(form, labnum)
    computadores = dbHandler.retriveLab(labnum)
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores, form=form)
  else:
    form = callForm()
    computadores = dbHandler.retriveLab(labnum)
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores, form=form)

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  computadores = dbHandler.retriveLab(labnum)
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores)

@app.route('/tecnico')
def tecnico():
  return render_template('tecnico.html')

if __name__ == '__main__':
  app.run(debug=True)