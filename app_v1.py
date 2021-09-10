# importação principal
from flask import Flask

# Definindo o App
app = Flask(__name__)

# Criando uma rota... há duas maneiras de fazer isso: Decorator ou Por Função
@app.route("/")
def index():
    return "Uma rota 'Index' inicial do Flask."

# Criando rota por regra
def minhaRotaTeste():
    return '<h3>Minha Rota!</h3>'
app.add_url_rule('/rotateste', "rotateste", minhaRotaTeste)

# Criando rota dinâmica

# Coloque o caracter "/" no fim, para evitar erros ao digitar ".../teste/hello/"
# Acrescente a rota @app.route("/teste/") para aceitar somente a chamada ".../hello"
# Função com parâmetro nome com o valor padrão igual a 'vazio'
@app.route("/hello/")
@app.route("/hello/<nome>/")
def hello(nome="vazio"):
    return "<p>Uma rota com nome {}</p>".format(nome)

# Criando rota com parâmetro do tipo inteiro
@app.route("/blog/")
@app.route("/blog/<int:postID>/")
def blog(postID=-1):
    if (postID >= 0):
        return "<p>Blog info {}</p>".format(postID)
    else: return "<p>Sem postID para o blog.</p>"

# Verifica se a aplicação que está sendo executada é a principal
if __name__ == '__main__':
    #app.run() <== Básica padrão
    app.run(debug=True, port=8081, host='127.0.0.1')