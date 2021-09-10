# importação principal
from flask import Flask, redirect, url_for

# Definindo o App
app = Flask(__name__)

# Criando uma rota... há duas maneiras de fazer isso: Decorator ou Por Função
@app.route("/")
def index():
    return "Uma rota 'Index' inicial do Flask."

# Criando redirecionamento de rotas
@app.route("/admin/")
def adminUser():
    return "<h3>Admin User!</h3>"

@app.route("/guest/")
@app.route("/guest/<name_user>")
def guest(name_user="No name"):
    return "<p>Guest user %s</p>" % name_user

@app.route("/user/")
@app.route("/user/<login>")
def admin(login=""):
    if login == "admin":
        return redirect(url_for('adminUser'))
    else:
        return redirect(url_for('guest', name_user=login))

@app.route("/site")
def siteGoogle():
    return redirect("https://google.com")

# Verifica se a aplicação que está sendo executada é a principal
if __name__ == '__main__':
    app.run()

