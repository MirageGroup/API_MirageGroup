from flask import Flask, render_template, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_session import Session
import db as dbHandler
from models.forms import callForm, accessForm , addComputer

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL(app)
Session(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
  form = accessForm()
  if form.validate_on_submit():
    acesso = dbHandler.retrieveAccessCode()
    if form.codigo.data != acesso[0][0]:
      flash('Código de acesso inválido')
      return render_template('index.html', form=form)
    else:
      session['key'] = 'tecnico'
      return redirect('/tecnico')
  return render_template('index.html', form=form)

@app.route('/lab/<int:labnum>', methods = ['POST', 'GET'])
def lab(labnum):
  if request.method == 'POST':
    form = callForm()
    if form.validate_on_submit():
      dbHandler.createCall(form, labnum)
    return redirect(f'/lab/{labnum}')
  else:
    form = callForm()
    computadores = dbHandler.retrieveLab(labnum)
    session['laboratorio'] = computadores
    componentes = dbHandler.retrieveComponents(labnum)
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores,componentes = componentes , form=form)

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  computadores = session['laboratorio']
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores)

@app.route('/lab/<int:labnum>/edit/salvar', methods=['POST', 'GET'])
def salvar(labnum):
  if request.method == 'POST':
    posicoes_layout = request.form['ids'].split(',')
    laboratorio = session['laboratorio']
    dbHandler.saveLayoutPositions(posicoes_layout, laboratorio ,labnum)
    return redirect(f'/lab/{labnum}/edit')

@app.route('/lab/<int:labnum>/<string:config>', methods = ['GET', 'POST'])
def alterar_componente(labnum, config):
  if request.method == 'POST':
    componente = request.form['componente']
    dbHandler.updateComponent(componente, labnum, config)
    return redirect(f'/lab/{labnum}')

@app.route('/tecnico', methods = ['POST', 'GET'])
def tecnico():
  if not session.get('key'):
    return redirect('/')
  chamadosAbertos = dbHandler.retrieveCalls('aberto')
  chamadosFechados = dbHandler.retrieveCalls('fechado')
  return render_template('tecnico.html', chamadosAbertos=chamadosAbertos, chamadosFechados=chamadosFechados)

@app.route('/tecnico/finishcall/<int:callnumber>')
def finishCall(callnumber):
  dbHandler.finishCall(callnumber)
  return redirect('/tecnico')
  
@app.route('/tecnico/sair')
def tecnico_sair():
  session.pop('key', None)
  return redirect('/')





if __name__ == '__main__':
  app.run(debug=True)