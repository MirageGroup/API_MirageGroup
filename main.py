from flask import Flask, render_template, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_session import Session
import db as dbHandler
from models.forms import callForm, accessForm

app = Flask(__name__)
app.config.from_object('config')

mysql = MySQL(app)
Session(app)

@app.route('/')
def home():
  acessForm_ = accessForm()
  return render_template('index.html',acessForm_=acessForm_)

@app.route('/verificacao' , methods = ["POST", "GET"])
def TecVerificacao():
  acessForm_ = accessForm()
  if acessForm_.validate_on_submit():
    acesso = dbHandler.retrieveAccessCode()
    if acessForm_ .codigo.data != acesso[0][0]:
       flash('Código de acesso inválido')
       return redirect('/')
    else:
      session['key'] = 'tecnico'
      return redirect('/tecnico')
  return render_template('index.html')
  
@app.route('/lab/<int:labnum>', methods = ['POST', 'GET'])
def lab(labnum):
  acessForm_ = accessForm()
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
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores,componentes = componentes , form=form, acessForm_=acessForm_)

@app.route('/lab/<int:labnum>/<string:config>', methods = ['GET', 'POST'])
def alterar_componente(labnum, config):
  if request.method == 'POST':
    componente = request.form['componente']
    dbHandler.updateComponent(componente, labnum, config)
    return redirect(f'/lab/{labnum}')

@app.route('/tecnico', methods = ['POST', 'GET'])
def tecnico():
  if not session.get('key'):
    return redirect('/modal')
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

  #  lista de chamados por sala
  Problem301 = dbHandler.retrieveNumberInLabs('301')
  Problem302 = dbHandler.retrieveNumberInLabs('302')
  Problem303 = dbHandler.retrieveNumberInLabs('303')
  Problem401 = dbHandler.retrieveNumberInLabs('401')
  Problem402 = dbHandler.retrieveNumberInLabs('402')
  Problem403 = dbHandler.retrieveNumberInLabs('403')
  Problem404 = dbHandler.retrieveNumberInLabs('404')
  Problem405 = dbHandler.retrieveNumberInLabs('405')
  Problem406 = dbHandler.retrieveNumberInLabs('406')
  Problem407 = dbHandler.retrieveNumberInLabs('407')
  Problem408 = dbHandler.retrieveNumberInLabs('408')
  Problem409 = dbHandler.retrieveNumberInLabs('409')
  Problem410 = dbHandler.retrieveNumberInLabs('410')
  Problem411 = dbHandler.retrieveNumberInLabs('411')
  Problem412 = dbHandler.retrieveNumberInLabs('412')

    

  return render_template('estatisticas.html',

    totalChamados = totalChamados,

    chamadosAbertos = chamadosAbertos,
    chamadosFechados = chamadosFechados,

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


  Problem301 = Problem301,
  Problem302 = Problem302,
  Problem303 = Problem303,
  Problem401 = Problem401,
  Problem402 = Problem402,
  Problem403 = Problem403,
  Problem404 = Problem404,
  Problem405 = Problem405,
  Problem406 = Problem406,
  Problem407 = Problem407,
  Problem408 = Problem408,
  Problem409 = Problem409,
  Problem410 = Problem410,
  Problem411 = Problem411,
  Problem412 = Problem412,
     
    )

if __name__ == '__main__':
  app.run(debug=True)