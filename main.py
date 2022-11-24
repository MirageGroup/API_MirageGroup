from flask import Flask, render_template, request, redirect, flash, session
from flask_mysqldb import MySQL
from flask_session import Session
import db as dbHandler
from models.forms import callForm, accessForm , addComputer

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
    session['laboratorio'] = computadores
    session['componentes'] = componentes
    return render_template('laboratorio.html', labnum=labnum, computadores=computadores,componentes = componentes , form=form, acessForm_=acessForm_)

@app.route('/lab/<int:labnum>/edit')
def lab_edit(labnum):
  computadores = session['laboratorio']
  componentes = session['componentes']
  return render_template('laboratorio_editor.html', labnum=labnum, computadores=computadores, componentes=componentes)

@app.route('/lab/<int:labnum>/edit/salvar', methods=['POST', 'GET'])
def salvar(labnum):
  if request.method == 'POST':
    layout_novo = request.form['layout']
    pc_novos_id = request.form['new_pcs']
    pc_novos_pos = request.form['new_pos']
    remover_pcs_ids = request.form['remove_pcs']
    if remover_pcs_ids:
      remover_pcs_ids = remover_pcs_ids.split(',')
      dbHandler.removePcs(remover_pcs_ids, labnum)
    if pc_novos_id:
      pc_novos_id = pc_novos_id.split(',')
      pc_novos_pos = pc_novos_pos.split(',')
      dbHandler.addNewPcs(pc_novos_id, pc_novos_pos, labnum)
    if layout_novo:
      layout_novo = layout_novo.split(',')
      dbHandler.saveLayoutPositions(layout_novo, labnum)
    return redirect(f'/lab/{labnum}')

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

@app.route('/tecnico/finishcall/<int:callnumber>')
def finishCall(callnumber):
  dbHandler.finishCall(callnumber)
  return redirect('/tecnico')

@app.route('/tecnico/deleteCall/<int:callnumber>')
def deleteCall(callnumber):
  dbHandler.deleteCall(callnumber)
  return redirect('/tecnico')
  
@app.route('/tecnico/sair')
def tecnico_sair():
  session.pop('key', None)
  return redirect('/')

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

  return render_template('estatisticas.html',
  totalChamados = totalChamados,
  chamadosAbertos = chamadosAbertos,
  chamadosFechados = chamadosFechados,
  rota = "estatisticas1"
    
    )

@app.route('/estatisticas/compproblems')
def estatisticsCompProblems():
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
  rota = 'estatisticas2',
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

@app.route('/estatisticas/labproblems')
def estatisticsLabProblems():
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
    rota = 'estatisticas3',
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

      # ESTATISTICAS DE CADA LABORATORIO


@app.route('/estatisticas/eachlabproblems301')
def eachlabproblems301():

 

  # PROBLEMAS 301
  Problems301 = dbHandler.numberOfProblemsInLab(301)
  Problem301Ligar = Problems301[0]
  Problem301NoInternet = Problems301[1]
  Problem301Lento = Problems301[2]
  Problem301NoImage = Problems301[3]
  Problem301NoSound = Problems301[4]
  Problem301BlueScreen = Problems301[5]
  Problem301TurnOff = Problems301[6]
  Problem301Initialization = Problems301[7]
  Problem301FreezingScreen = Problems301[8]
  Problem301Mouse = Problems301[9]
  Problem301Board = Problems301[10]
  Problem301Other = Problems301[11]
  return render_template('estatisticas.html',
    rota = 'estatisticas301',
    # PROBLEMAS 301
  Problem301Ligar =  Problem301Ligar,
  Problem301NoInternet = Problem301NoInternet,
  Problem301Lento =   Problem301Lento,
  Problem301NoImage = Problem301NoImage,
  Problem301NoSound = Problem301NoSound,
  Problem301BlueScreen = Problem301BlueScreen,
  Problem301TurnOff =  Problem301TurnOff,
  Problem301Initialization =  Problem301Initialization,
  Problem301FreezingScreen = Problem301FreezingScreen,
  Problem301Mouse = Problem301Mouse,
  Problem301Board =  Problem301Board,
  Problem301Other = Problem301Other,
  )

@app.route('/estatisticas/eachlabproblems302')
def eachlabproblems302():
  # PROBLEMAS 302
  Problems302 = dbHandler.numberOfProblemsInLab(302)
  Problem302Ligar = Problems302[0]
  Problem302NoInternet = Problems302[1]
  Problem302Lento = Problems302[2]
  Problem302NoImage = Problems302[3]
  Problem302NoSound = Problems302[4]
  Problem302BlueScreen = Problems302[5]
  Problem302TurnOff = Problems302[6]
  Problem302Initialization = Problems302[7]
  Problem302FreezingScreen = Problems302[8]
  Problem302Mouse = Problems302[9]
  Problem302Board = Problems302[10]
  Problem302Other = Problems302[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas302',
   # PROBLEMAS 302
  Problem302Ligar =  Problem302Ligar,
  Problem302NoInternet = Problem302NoInternet,
  Problem302Lento =   Problem302Lento,
  Problem302NoImage = Problem302NoImage,
  Problem302NoSound = Problem302NoSound,
  Problem302BlueScreen = Problem302BlueScreen,
  Problem302TurnOff =  Problem302TurnOff,
  Problem302Initialization =  Problem302Initialization,
  Problem302FreezingScreen = Problem302FreezingScreen,
  Problem302Mouse = Problem302Mouse,
  Problem302Board =  Problem302Board,
  Problem302Other = Problem302Other,)


@app.route('/estatisticas/eachlabproblems303')
def eachlabproblems303():
  
  # PROBLEMAS 303
  Problems303 = dbHandler.numberOfProblemsInLab(303)
  Problem303Ligar = Problems303[0]
  Problem303NoInternet = Problems303[1]
  Problem303Lento = Problems303[2]
  Problem303NoImage = Problems303[3]
  Problem303NoSound = Problems303[4]
  Problem303BlueScreen = Problems303[5]
  Problem303TurnOff = Problems303[6]
  Problem303Initialization = Problems303[7]
  Problem303FreezingScreen = Problems303[8]
  Problem303Mouse = Problems303[9]
  Problem303Board = Problems303[10]
  Problem303Other = Problems303[11]
  return render_template('estatisticas.html',  
  rota = 'estatisticas303',
  # PROBLEMAS 303
  
  Problem303Ligar =  Problem303Ligar,
  Problem303NoInternet = Problem303NoInternet,
  Problem303Lento =   Problem303Lento,
  Problem303NoImage = Problem303NoImage,
  Problem303NoSound = Problem303NoSound,
  Problem303BlueScreen = Problem303BlueScreen,
  Problem303TurnOff =  Problem303TurnOff,
  Problem303Initialization =  Problem303Initialization,
  Problem303FreezingScreen = Problem303FreezingScreen,
  Problem303Mouse = Problem303Mouse,
  Problem303Board =  Problem303Board,
  Problem303Other = Problem303Other,
  )

@app.route('/estatisticas/eachlabproblems401')
def eachlabproblems401():
  # PROBLEMAS 401
  Problems401 = dbHandler.numberOfProblemsInLab(401)
  Problem401Ligar = Problems401[0]
  Problem401NoInternet = Problems401[1]
  Problem401Lento = Problems401[2]
  Problem401NoImage = Problems401[3]
  Problem401NoSound = Problems401[4]
  Problem401BlueScreen = Problems401[5]
  Problem401TurnOff = Problems401[6]
  Problem401Initialization = Problems401[7]
  Problem401FreezingScreen = Problems401[8]
  Problem401Mouse = Problems401[9]
  Problem401Board = Problems401[10]
  Problem401Other = Problems401[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas401',
    # PROBLEMAS 401
  
  Problem401Ligar =  Problem401Ligar,
  Problem401NoInternet = Problem401NoInternet,
  Problem401Lento =   Problem401Lento,
  Problem401NoImage = Problem401NoImage,
  Problem401NoSound = Problem401NoSound,
  Problem401BlueScreen = Problem401BlueScreen,
  Problem401TurnOff =  Problem401TurnOff,
  Problem401Initialization =  Problem401Initialization,
  Problem401FreezingScreen = Problem401FreezingScreen,
  Problem401Mouse = Problem401Mouse,
  Problem401Board =  Problem401Board,
  Problem401Other = Problem401Other,)

@app.route('/estatisticas/eachlabproblems402')
def eachlabproblems402():
   # PROBLEMAS 402
  Problems402 = dbHandler.numberOfProblemsInLab(402)
  Problem402Ligar = Problems402[0]
  Problem402NoInternet = Problems402[1]
  Problem402Lento = Problems402[2]
  Problem402NoImage = Problems402[3]
  Problem402NoSound = Problems402[4]
  Problem402BlueScreen = Problems402[5]
  Problem402TurnOff = Problems402[6]
  Problem402Initialization = Problems402[7]
  Problem402FreezingScreen = Problems402[8]
  Problem402Mouse = Problems402[9]
  Problem402Board = Problems402[10]
  Problem402Other = Problems402[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas402',
  # PROBLEMAS 402
  
  Problem402Ligar =  Problem402Ligar,
  Problem402NoInternet = Problem402NoInternet,
  Problem402Lento =   Problem402Lento,
  Problem402NoImage = Problem402NoImage,
  Problem402NoSound = Problem402NoSound,
  Problem402BlueScreen = Problem402BlueScreen,
  Problem402TurnOff =  Problem402TurnOff,
  Problem402Initialization =  Problem402Initialization,
  Problem402FreezingScreen = Problem402FreezingScreen,
  Problem402Mouse = Problem402Mouse,
  Problem402Board =  Problem402Board,
  Problem402Other = Problem402Other,)

@app.route('/estatisticas/eachlabproblems403')
def eachlabproblems403():
    # PROBLEMAS 403
  Problems403 = dbHandler.numberOfProblemsInLab(403)
  Problem403Ligar = Problems403[0]
  Problem403NoInternet = Problems403[1]
  Problem403Lento = Problems403[2]
  Problem403NoImage = Problems403[3]
  Problem403NoSound = Problems403[4]
  Problem403BlueScreen = Problems403[5]
  Problem403TurnOff = Problems403[6]
  Problem403Initialization = Problems403[7]
  Problem403FreezingScreen = Problems403[8]
  Problem403Mouse = Problems403[9]
  Problem403Board = Problems403[10]
  Problem403Other = Problems403[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas403',
   # PROBLEMAS 403
  
  Problem403Ligar =  Problem403Ligar,
  Problem403NoInternet = Problem403NoInternet,
  Problem403Lento =   Problem403Lento,
  Problem403NoImage = Problem403NoImage,
  Problem403NoSound = Problem403NoSound,
  Problem403BlueScreen = Problem403BlueScreen,
  Problem403TurnOff =  Problem403TurnOff,
  Problem403Initialization =  Problem403Initialization,
  Problem403FreezingScreen = Problem403FreezingScreen,
  Problem403Mouse = Problem403Mouse,
  Problem403Board =  Problem403Board,
  Problem403Other = Problem403Other,)


@app.route('/estatisticas/eachlabproblems404')
def eachlabproblems404():
    # PROBLEMAS 404
  Problems404 = dbHandler.numberOfProblemsInLab(404)
  Problem404Ligar = Problems404[0]
  Problem404NoInternet = Problems404[1]
  Problem404Lento = Problems404[2]
  Problem404NoImage = Problems404[3]
  Problem404NoSound = Problems404[4]
  Problem404BlueScreen = Problems404[5]
  Problem404TurnOff = Problems404[6]
  Problem404Initialization = Problems404[7]
  Problem404FreezingScreen = Problems404[8]
  Problem404Mouse = Problems404[9]
  Problem404Board = Problems404[10]
  Problem404Other = Problems404[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas404',
  # PROBLEMAS 404
  
  Problem404Ligar =  Problem404Ligar,
  Problem404NoInternet = Problem404NoInternet,
  Problem404Lento =   Problem404Lento,
  Problem404NoImage = Problem404NoImage,
  Problem404NoSound = Problem404NoSound,
  Problem404BlueScreen = Problem404BlueScreen,
  Problem404TurnOff =  Problem404TurnOff,
  Problem404Initialization =  Problem404Initialization,
  Problem404FreezingScreen = Problem404FreezingScreen,
  Problem404Mouse = Problem404Mouse,
  Problem404Board =  Problem404Board,
  Problem404Other = Problem404Other,)

@app.route('/estatisticas/eachlabproblems405')
def eachlabproblems405():
    # PROBLEMAS 405
  Problems405 = dbHandler.numberOfProblemsInLab(405)
  Problem405Ligar = Problems405[0]
  Problem405NoInternet = Problems405[1]
  Problem405Lento = Problems405[2]
  Problem405NoImage = Problems405[3]
  Problem405NoSound = Problems405[4]
  Problem405BlueScreen = Problems405[5]
  Problem405TurnOff = Problems405[6]
  Problem405Initialization = Problems405[7]
  Problem405FreezingScreen = Problems405[8]
  Problem405Mouse = Problems405[9]
  Problem405Board = Problems405[10]
  Problem405Other = Problems405[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas405',
  # PROBLEMAS 405
  
  Problem405Ligar =  Problem405Ligar,
  Problem405NoInternet = Problem405NoInternet,
  Problem405Lento =   Problem405Lento,
  Problem405NoImage = Problem405NoImage,
  Problem405NoSound = Problem405NoSound,
  Problem405BlueScreen = Problem405BlueScreen,
  Problem405TurnOff =  Problem405TurnOff,
  Problem405Initialization =  Problem405Initialization,
  Problem405FreezingScreen = Problem405FreezingScreen,
  Problem405Mouse = Problem405Mouse,
  Problem405Board =  Problem405Board,
  Problem405Other = Problem405Other,
  )

@app.route('/estatisticas/eachlabproblems406')
def eachlabproblems406():
     # PROBLEMAS 406
  Problems406 = dbHandler.numberOfProblemsInLab(406)
  Problem406Ligar = Problems406[0]
  Problem406NoInternet = Problems406[1]
  Problem406Lento = Problems406[2]
  Problem406NoImage = Problems406[3]
  Problem406NoSound = Problems406[4]
  Problem406BlueScreen = Problems406[5]
  Problem406TurnOff = Problems406[6]
  Problem406Initialization = Problems406[7]
  Problem406FreezingScreen = Problems406[8]
  Problem406Mouse = Problems406[9]
  Problem406Board = Problems406[10]
  Problem406Other = Problems406[11]
  return render_template('estatisticas.html',
  rota = 'estatisticas406',

   # PROBLEMAS 406
  Problem406Ligar =  Problem406Ligar,
  Problem406NoInternet = Problem406NoInternet,
  Problem406Lento =   Problem406Lento,
  Problem406NoImage = Problem406NoImage,
  Problem406NoSound = Problem406NoSound,
  Problem406BlueScreen = Problem406BlueScreen,
  Problem406TurnOff =  Problem406TurnOff,
  Problem406Initialization =  Problem406Initialization,
  Problem406FreezingScreen = Problem406FreezingScreen,
  Problem406Mouse = Problem406Mouse,
  Problem406Board =  Problem406Board,
  Problem406Other = Problem406Other,
  )

@app.route('/estatisticas/eachlabproblems407')
def eachlabproblems407():
    # PROBLEMAS 407
  Problems407 = dbHandler.numberOfProblemsInLab(407)
  Problem407Ligar = Problems407[0]
  Problem407NoInternet = Problems407[1]
  Problem407Lento = Problems407[2]
  Problem407NoImage = Problems407[3]
  Problem407NoSound = Problems407[4]
  Problem407BlueScreen = Problems407[5]
  Problem407TurnOff = Problems407[6]
  Problem407Initialization = Problems407[7]
  Problem407FreezingScreen = Problems407[8]
  Problem407Mouse = Problems407[9]
  Problem407Board = Problems407[10]
  Problem407Other = Problems407[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas407',
 
  # PROBLEMAS 407
  Problem407Ligar =  Problem407Ligar,
  Problem407NoInternet = Problem407NoInternet,
  Problem407Lento =   Problem407Lento,
  Problem407NoImage = Problem407NoImage,
  Problem407NoSound = Problem407NoSound,
  Problem407BlueScreen = Problem407BlueScreen,
  Problem407TurnOff =  Problem407TurnOff,
  Problem407Initialization =  Problem407Initialization,
  Problem407FreezingScreen = Problem407FreezingScreen,
  Problem407Mouse = Problem407Mouse,
  Problem407Board =  Problem407Board,
  Problem407Other = Problem407Other,)


@app.route('/estatisticas/eachlabproblems408')
def eachlabproblems408():
     
  # PROBLEMAS 408
  Problems408 = dbHandler.numberOfProblemsInLab(408)
  Problem408Ligar = Problems408[0]
  Problem408NoInternet = Problems408[1]
  Problem408Lento = Problems408[2]
  Problem408NoImage = Problems408[3]
  Problem408NoSound = Problems408[4]
  Problem408BlueScreen = Problems408[5]
  Problem408TurnOff = Problems408[6]
  Problem408Initialization = Problems408[7]
  Problem408FreezingScreen = Problems408[8]
  Problem408Mouse = Problems408[9]
  Problem408Board = Problems408[10]
  Problem408Other = Problems408[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas408',
  # PROBLEMAS 408
  
  Problem408Ligar =  Problem408Ligar,
  Problem408NoInternet = Problem408NoInternet,
  Problem408Lento =   Problem408Lento,
  Problem408NoImage = Problem408NoImage,
  Problem408NoSound = Problem408NoSound,
  Problem408BlueScreen = Problem408BlueScreen,
  Problem408TurnOff =  Problem408TurnOff,
  Problem408Initialization =  Problem408Initialization,
  Problem408FreezingScreen = Problem408FreezingScreen,
  Problem408Mouse = Problem408Mouse,
  Problem408Board =  Problem408Board,
  Problem408Other = Problem408Other,)

@app.route('/estatisticas/eachlabproblems409')
def eachlabproblems409():
    # PROBLEMAS 409
  Problems409 = dbHandler.numberOfProblemsInLab(409)
  Problem409Ligar = Problems409[0]
  Problem409NoInternet = Problems409[1]
  Problem409Lento = Problems409[2]
  Problem409NoImage = Problems409[3]
  Problem409NoSound = Problems409[4]
  Problem409BlueScreen = Problems409[5]
  Problem409TurnOff = Problems409[6]
  Problem409Initialization = Problems409[7]
  Problem409FreezingScreen = Problems409[8]
  Problem409Mouse = Problems409[9]
  Problem409Board = Problems409[10]
  Problem409Other = Problems409[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas409',
  # PROBLEMAS 409
  
  Problem409Ligar =  Problem409Ligar,
  Problem409NoInternet = Problem409NoInternet,
  Problem409Lento =   Problem409Lento,
  Problem409NoImage = Problem409NoImage,
  Problem409NoSound = Problem409NoSound,
  Problem409BlueScreen = Problem409BlueScreen,
  Problem409TurnOff =  Problem409TurnOff,
  Problem409Initialization =  Problem409Initialization,
  Problem409FreezingScreen = Problem409FreezingScreen,
  Problem409Mouse = Problem409Mouse,
  Problem409Board =  Problem409Board,
  Problem409Other = Problem409Other,)

@app.route('/estatisticas/eachlabproblems410')
def eachlabproblems410():
    # PROBLEMAS 410
  Problems410 = dbHandler.numberOfProblemsInLab(410)
  Problem410Ligar = Problems410[0]
  Problem410NoInternet = Problems410[1]
  Problem410Lento = Problems410[2]
  Problem410NoImage = Problems410[3]
  Problem410NoSound = Problems410[4]
  Problem410BlueScreen = Problems410[5]
  Problem410TurnOff = Problems410[6]
  Problem410Initialization = Problems410[7]
  Problem410FreezingScreen = Problems410[8]
  Problem410Mouse = Problems410[9]
  Problem410Board = Problems410[10]
  Problem410Other = Problems410[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas410',
  # PROBLEMAS 410
  
  Problem410Ligar =  Problem410Ligar,
  Problem410NoInternet = Problem410NoInternet,
  Problem410Lento =   Problem410Lento,
  Problem410NoImage = Problem410NoImage,
  Problem410NoSound = Problem410NoSound,
  Problem410BlueScreen = Problem410BlueScreen,
  Problem410TurnOff =  Problem410TurnOff,
  Problem410Initialization =  Problem410Initialization,
  Problem410FreezingScreen = Problem410FreezingScreen,
  Problem410Mouse = Problem410Mouse,
  Problem410Board =  Problem410Board,
  Problem410Other = Problem410Other,)

@app.route('/estatisticas/eachlabproblems411')
def eachlabproblems411():
     # PROBLEMAS 411
  Problems411 = dbHandler.numberOfProblemsInLab(411)
  Problem411Ligar = Problems411[0]
  Problem411NoInternet = Problems411[1]
  Problem411Lento = Problems411[2]
  Problem411NoImage = Problems411[3]
  Problem411NoSound = Problems411[4]
  Problem411BlueScreen = Problems411[5]
  Problem411TurnOff = Problems411[6]
  Problem411Initialization = Problems411[7]
  Problem411FreezingScreen = Problems411[8]
  Problem411Mouse = Problems411[9]
  Problem411Board = Problems411[10]
  Problem411Other = Problems411[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas411',
  # PROBLEMAS 411
  
  Problem411Ligar =  Problem411Ligar,
  Problem411NoInternet = Problem411NoInternet,
  Problem411Lento =   Problem411Lento,
  Problem411NoImage = Problem411NoImage,
  Problem411NoSound = Problem411NoSound,
  Problem411BlueScreen = Problem411BlueScreen,
  Problem411TurnOff =  Problem411TurnOff,
  Problem411Initialization =  Problem411Initialization,
  Problem411FreezingScreen = Problem411FreezingScreen,
  Problem411Mouse = Problem411Mouse,
  Problem411Board =  Problem411Board,
  Problem411Other = Problem411Other,
)

@app.route('/estatisticas/eachlabproblems412')
def eachlabproblems412():
     # PROBLEMAS 412
  Problems412 = dbHandler.numberOfProblemsInLab(412)
  Problem412Ligar = Problems412[0]
  Problem412NoInternet = Problems412[1]
  Problem412Lento = Problems412[2]
  Problem412NoImage = Problems412[3]
  Problem412NoSound = Problems412[4]
  Problem412BlueScreen = Problems412[5]
  Problem412TurnOff = Problems412[6]
  Problem412Initialization = Problems412[7]
  Problem412FreezingScreen = Problems412[8]
  Problem412Mouse = Problems412[9]
  Problem412Board = Problems412[10]
  Problem412Other = Problems412[11]

  return render_template('estatisticas.html',
  rota = 'estatisticas412',
  # PROBLEMAS 412
  
  Problem412Ligar =  Problem412Ligar,
  Problem412NoInternet = Problem412NoInternet,
  Problem412Lento =   Problem412Lento,
  Problem412NoImage = Problem412NoImage,
  Problem412NoSound = Problem412NoSound,
  Problem412BlueScreen = Problem412BlueScreen,
  Problem412TurnOff =  Problem412TurnOff,
  Problem412Initialization =  Problem412Initialization,
  Problem412FreezingScreen = Problem412FreezingScreen,
  Problem412Mouse = Problem412Mouse,
  Problem412Board =  Problem412Board,
  Problem412Other = Problem412Other,)
  

if __name__ == '__main__':
  app.run(debug=True)