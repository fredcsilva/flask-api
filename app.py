# importação principal
from flask import Flask

# Definindo o App
app = Flask(__name__)

# Criando uma rota... há duas maneiras de fazer isso: Decorator ou Por Função
@app.route("/")
def index():
    return "Uma rota 'Index' inicial do Flask."

# Verifica se a aplicação que está sendo executada é a principal
if __name__ == '__main__':
    app.run()

