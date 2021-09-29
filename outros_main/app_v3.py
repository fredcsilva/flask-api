from flask import Flask, request

# Trabalhando com arquivos estáticos e métodos HTTP
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return "App started."

# Principais métodos
# GET, POST, PUT, PATCH, DELETE
@app.route("/add", methods=["GET", "POST"])
def add():
    metodo = ""
    if request.method == "GET":
        metodo = "GET"
    elif request.method == "POST":
        metodo = "POST"
    else:
        metodo = "NO METHOD"
    return "Método Add {}".format(metodo)

if __name__ == "__main__":
    app.run(debug=True)