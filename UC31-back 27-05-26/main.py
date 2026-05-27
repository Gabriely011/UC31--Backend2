from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('formulario.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    return "{} e {}".format(usuario, senha)



if __name__ == '__main__':
    app.run(debug=True)