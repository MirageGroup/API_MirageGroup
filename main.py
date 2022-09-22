from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config.update(
  TEMPLATES_AUTO_RELOAD = True
)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/lab')
def lab():
  return render_template('laboratorio.html')

@app.route('/lab_edit')
def lab_edit():
  return render_template('laboratorio_editor.html')

if __name__ == '__main__':
  app.run(debug=True)