from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""

    if request.method == "POST":
        nickname = request.form.get("nickname")
        jogo = request.form.get("jogo")
        email = request.form.get("email")

        if nickname == "" or jogo == "" or email == "" or len(nickname) < 4:
            mensagem = "Preencha todos os campos obrigatórios."
        else:
            mensagem = "Inscrição realizada com sucesso!"

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)