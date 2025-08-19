from flask import Flask, render_template #importa a biblioteca flask

#criando uma instancia da classe Flask

app = Flask(__name__, template_folder = 'views') #__name__ é uma variavel especial que representa o nome do modulo python que esta sendo executado


#criando uma rota para a pagina inicial
@app.route('/')
def home():
    return render_template('index.html')

#criando uma rota para a pagina de games
@app.route('/games')
def games():
    title = 'Oi yasmin te amo muito!!!!!!!!'
    year = 2015
    category = 'Ação'
    players = ['João', 'Maria', 'Pedro', 'Ana']
    console = {'name' : 'Playstation 5', 'manufacturer' : 'Sony', 'year' : '2020'}
    return render_template('games.html', title = title, year = year, category = category, players = players, console = console)
#se for executado diretamente, o app.run() é executado
if __name__ == '__main__':
    app.run(debug = True, port = 2706, host = 'localhost')



