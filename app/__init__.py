from flask import Flask
from flask_sqlalchemy import SQLAlchemy # (Import principal do SQLAlchemy)
from flask_migrate import Migrate

import config
# from flask_script import Manager

app = Flask(__name__)

from .controllers import index_controller

app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts_twitter.db' # (Banco de Dados SQLite)
db = SQLAlchemy(app) # (Criando uma instância padrão db)
migrate = Migrate(app, db) # Instancia o Migrate

# O Manager se preocupa com os comandos de inicialização
# manager = Manager(app)

