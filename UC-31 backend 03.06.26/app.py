from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    erros = []

    # Recebendo e tratando os dados
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    cpf = request.form.get('cpf', '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso = request.form.get('curso', '').strip()
    idade = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '').strip()

    # Tratamento telefone
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")
    telefone = telefone.replace(" ", "")

    # Tratamento CPF
    cpf = cpf.replace(".", "")
    cpf = cpf.replace("-", "")

    # Verificação campos obrigatórios
    campos = [nome, email, telefone, cpf, cidade, estado, curso, idade, senha]

    if "" in campos:
        erros.append("Preencha todos os campos obrigatórios.")

    # Nome
    if len(nome) < 8:
        erros.append("Nome inválido.")

    # Email
    if '@' not in email or '.com' not in email:
        erros.append("E-mail inválido.")

    # Telefone
    if not telefone.isdigit() or len(telefone) != 11:
        erros.append("Telefone inválido.")

    # CPF
    if not cpf.isdigit() or len(cpf) != 11:
        erros.append("CPF inválido.")

    # Cidade
    if len(cidade) < 3:
        erros.append("Cidade inválida.")

    # Estado
    if len(estado) != 2 or not estado.isalpha():
        erros.append("Estado inválido.")

    # Curso
    if curso == "":
        erros.append("Curso inválido.")

    # Idade
    if not idade.isdigit():
        erros.append("Idade inválida.")
    else:
        if int(idade) < 16:
            erros.append("Idade mínima é 16 anos.")

    # Senha
    possui_numero = any(caractere.isdigit() for caractere in senha)

    if len(senha) < 8 or not possui_numero:
        erros.append("Senha muito fraca.")

    # Se houver erros
    if erros:
        return render_template(
            'resultado.html',
            sucesso=False,
            erros=erros
        )

    # Cadastro válido
    return render_template(
        'resultado.html',
        sucesso=True,
        nome=nome,
        email=email,
        telefone=telefone,
        cpf=cpf,
        cidade=cidade,
        estado=estado,
        curso=curso,
        idade=idade
    )


if __name__ == '__main__':
    app.run(debug=True)