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

@app.route('/lab/submit', methods = ['POST', 'GET'])
def lab_submit():
  if request.method == 'POST':
    number = request.form['number']
    category = request.form['category']
    description = request.form['description']

    print(number)
    print(category)
    print(description)

    return render_template('laboratorio.html')


if __name__ == '__main__':
  app.run(debug=True)