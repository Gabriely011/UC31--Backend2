from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "taskmanager123"


def obter_tarefas():
    return session.get("tarefas", [])


def salvar_tarefas(tarefas):
    session["tarefas"] = tarefas


@app.route("/")
def index():
    tarefas = obter_tarefas()

    total = len(tarefas)
    concluidas = sum(1 for tarefa in tarefas if tarefa["feita"])
    pendentes = total - concluidas

    progresso = 0
    if total > 0:
        progresso = round((concluidas / total) * 100)

    return render_template(
        "index.html",
        tarefas=tarefas,
        total=total,
        concluidas=concluidas,
        pendentes=pendentes,
        progresso=progresso
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():

    descricao = request.form.get("tarefa")
    categoria = request.form.get("categoria")

    if descricao:

        tarefas = obter_tarefas()

        nova_tarefa = {
            "descricao": descricao,
            "categoria": categoria,
            "prioridade": "Alta",
            "feita": False
        }

        tarefas.append(nova_tarefa)
        salvar_tarefas(tarefas)

    return redirect(url_for("index"))


@app.route("/concluir/<int:id_tarefa>")
def concluir(id_tarefa):

    tarefas = obter_tarefas()

    if 0 <= id_tarefa < len(tarefas):
        tarefas[id_tarefa]["feita"] = True
        salvar_tarefas(tarefas)

    return redirect(url_for("index"))


@app.route("/excluir/<int:id_tarefa>")
def excluir(id_tarefa):

    tarefas = obter_tarefas()

    if 0 <= id_tarefa < len(tarefas):
        tarefas.pop(id_tarefa)
        salvar_tarefas(tarefas)

    return redirect(url_for("index"))


@app.route("/limpar")
def limpar():

    session.pop("tarefas", None)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)