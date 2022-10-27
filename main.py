from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import db as dbHandler
from models.forms import callForm, accessForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MirageGroup'

app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'bbc6f0cc739a84'
app.config['MYSQL_PASSWORD'] = '2c05d7ed'
app.config['MYSQL_DB'] = 'heroku_be80b7ca2ec9c96'

mysql = MySQL(app)

@app.route('/')
def home():
  form = accessForm()
  return render_template('index.html', form=form)

@app.route('/lab/<int:labnum>', methods = ['POST', 'GET'])
def lab(labnum):
  if request.method == 'POST':
    form = callForm()
    if form.validate_on_submit():
      dbHandler.createCall(form, labnum)
      computadores = dbHandler.retrieveLab(labnum)
    return redirect(f'/lab/{labnum}')
  else:
    form = callForm()
    computadores = dbHandler.retrieveLab(labnum)
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores, form=form)

@app.route('/tecnico', methods = ['POST', 'GET'])
def tecnico():
  chamados = dbHandler.retrieveCalls()
  return render_template('tecnico.html', chamados=chamados)

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  computadores = dbHandler.retrieveLab(labnum)
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores)

@app.route('/tecnico/finishcall/<int:callnumber>')
def finishCall(callnumber):
  dbHandler.finishCall(callnumber)
  return redirect('/tecnico')

if __name__ == '__main__':
  app.run(debug=True)