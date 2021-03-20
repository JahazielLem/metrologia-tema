from flask import Flask, render_template, flash, redirect, request
from flask.helpers import url_for
from flask_mail import Mail, Message 
   
app = Flask(__name__)

# configuration of mail 
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kevinleon.morales@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'kevinleon.morales@gmail.com'
app.config['MAIL_PASSWORD'] = '260195123As'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) 
   
# message object mapped to a particular URL ‘/’ 
@app.route('/') 
def index(): 
   return render_template('index.html')

@app.route('/servicios') 
def servicios(): 
   return render_template('servicios.html')


@app.route('/sendEmail', methods=('GET','POST'))
def sendEmail():
      nombre = request.form['nombre']
      email = request.form['email']
      asunto = request.form['asunto']
      numero = request.form['numero']
      comentarios = request.form['comentarios']
      stringData = "Nombre: {}\nEmail: {}\nNumero: {}\nComentarios: {}".format(nombre,email,numero,comentarios)
      msg = Message(asunto, recipients=['dewefi3825@lidte.com'])
      msg.html = '<p>Nombre: {}</p><br><p>Email: {}</p><br><p>Número {}</p><br><p>Comentarios: {}</p>'.format(nombre,email,numero,comentarios)
      mail.send(msg)
      flash('Se envio tu correo con exito, nos contactaremos cuanto antes.')
      return redirect(url_for('index'))

if __name__ == '__main__': 
   app.run(debug = True) 