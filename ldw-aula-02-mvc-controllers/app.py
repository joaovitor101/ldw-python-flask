from flask import Flask, render_template #importa a biblioteca flask
from controllers import routes
#criando uma instancia da classe Flask

app = Flask(__name__, template_folder='views', static_folder='static')
routes.init_app(app) 

if __name__ == '__main__':
    app.run(debug = True, port = 2706, host = 'localhost')



