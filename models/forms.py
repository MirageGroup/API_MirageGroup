from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length

choices = ['O computador não liga',
           'O computador está sem internet',
           'O computador está muito lento',
           'O computador não está dando imagem',
           'O computador está sem som',
           'O computador está tendo a tela azul',
           'O computador está desligando sozinho',
           'O sistema operacional não está inicializando',
           'A tela está congelando',
           'O mouse não está funcionando',
           'O teclado não está funcionando',
           'Outro'
          ]

class callForm(FlaskForm):
  input_numero_pc = StringField('input_numero_pc', validators=[DataRequired()])
  email = EmailField('email', validators=[DataRequired()])
  pc_problem = SelectField('pc_problem', validators=[DataRequired()], choices=choices)
  problem_description = TextAreaField('problem_description', validators=[DataRequired(), Length(min=10, max=350)])

class accessForm(FlaskForm):
  codigo = PasswordField('codigo', validators=[DataRequired()])