from flask import Flask, render_template, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_session import Session
import db as dbHandler
from models.forms import callForm, accessForm

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
    componentes = dbHandler.retrieveComponents(labnum)
    print(componentes)
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores,componentes = componentes , form=form)

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

@app.route('/tecnico/sair')
def tecnico_sair():
  session.pop('key', None)
  return redirect('/')

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  computadores = dbHandler.retrieveLab(labnum)
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores)

@app.route('/tecnico/finishcall/<int:callnumber>')
def finishCall(callnumber):
  dbHandler.finishCall(callnumber)
  return redirect('/tecnico')

@app.route('/tecnico/addcoment/<int:callnumber>', methods = ['POST', 'GET'])
def addcoment(callnumber):
  comentario = request.form['coment']
  dbHandler.addComentario(comentario, callnumber)
  return redirect('/tecnico')

@app.route('/estatisticas')
def estatistics():

  # TOTAIS DE CHAMADOS
  totalChamados = dbHandler.retrieveNumbersofCalls()
  print(totalChamados)

  # TOTAIS DE CHAMADOS ABERTOS OU FECHADOS
  chamadosAbertos = dbHandler.retrieveNumbersOpenOrClose("aberto")
  chamadosFechados = dbHandler.retrieveNumbersOpenOrClose("fechado")
  print(chamadosAbertos,chamadosFechados)

  # lista de problemas
  ProblemLigar = dbHandler.numberOfProblems('O computador não liga')
  ProblemNoInternet = dbHandler.numberOfProblems('O computador está sem internet')
  ProblemLento = dbHandler.numberOfProblems('O computador está muito lento')
  ProblemNoImage = dbHandler.numberOfProblems('O computador não está dando imagem')
  ProblemNoSound = dbHandler.numberOfProblems('O computador está sem som')
  ProblemBlueScreen = dbHandler.numberOfProblems('O computador está tendo a tela azul')
  ProblemTurnOff = dbHandler.numberOfProblems('O computador está desligando sozinho')
  ProblemInitialization = dbHandler.numberOfProblems('O sistema operacional não está inicializando')
  ProblemFreezingScreen = dbHandler.numberOfProblems('A tela está congelando')
  ProblemMouse = dbHandler.numberOfProblems('O mouse não está funcionando')
  ProblemBoard = dbHandler.numberOfProblems('O teclado não está funcionando')
  ProblemOther = dbHandler.numberOfProblems('Outro')

    

  return render_template('estatisticas.html',
    ProblemLigar = ProblemLigar,
    ProblemNoInternet = ProblemNoInternet,
    ProblemLento = ProblemLento,
    ProblemNoImage = ProblemNoImage,
    ProblemNoSound = ProblemNoSound,
    ProblemBlueScreen = ProblemBlueScreen,
    ProblemTurnOff = ProblemTurnOff,
    ProblemInitialization = ProblemInitialization,
    ProblemFreezingScreen = ProblemFreezingScreen,
    ProblemMouse = ProblemMouse,
    ProblemBoard = ProblemBoard,
    ProblemOther =  ProblemOther,





    
    
    
    )



if __name__ == '__main__':
  app.run(debug=True)