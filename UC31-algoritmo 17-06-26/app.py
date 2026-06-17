from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

@app.route("/contador")
def contador():
    session["acessos"] = session.get("acessos", 0) + 1
    return render_template("contador.html", contador=session["acessos"])

@app.route("/contador/zerar", methods=["POST"])
def zerar():
    session.pop("acessos", None) 
    return redirect(url_for("contador"))

if __name__ == "__main__":
    app.run(debug=True)