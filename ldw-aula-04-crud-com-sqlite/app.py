from flask import Flask, render_template #importa a biblioteca flask
from controllers import routes
#criando uma instancia da classe Flask
from models.database import db
#importanto biblioca para manipulação do S.O
import os

app = Flask(__name__, template_folder='views', static_folder='static')
routes.init_app(app) 
dir = os.path.abspath(os.path.dirname(__file__))
#configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir + os.path.join('models/games.sqlite3')
db.init_app(app)
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    db.init_app(app = app)
    #verificar no início da aplicação se o banco de dados existe, senão criar
    with app.test_request_context():
        db.create_all()
    
    app.run(debug = True, port = 5000, host = '0.0.0.0')



