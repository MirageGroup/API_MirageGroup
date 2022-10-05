from django.shortcuts import render
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import models as dbHandler


app = Flask('__name__')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config.update(
  TEMPLATES_AUTO_RELOAD = True
)

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
  return render_template('laboratorio.html', labnum=labnum)

@app.route('/lab_3')
def lab_3():
  return render_template('lab_3.html')

@app.route('/lab_edit')
def lab_edit():
  return render_template('laboratorio_editor.html')

if __name__ == '__main__':
  app.run(debug=True)#pode ser mudado para 127.0.0.1