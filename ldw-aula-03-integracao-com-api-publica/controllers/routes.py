from flask import render_template, request, redirect, url_for
import urllib.request
import json

def init_app(app):
    players = ['Yasmin', 'João', 'Apollo', 'Frederico']
    gamelist = [{'Título':'Cs 1.6', 'Ano':1996, 'Categoria':'FPS Online'}]
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/games', methods=["GET", "POST"])
    def games():
        nonlocal players
        title = 'CS-GO'
        year = 2012
        category = 'FPS Online'
        
        console = {'Nome': 'PC', 'Fabricante': 'Valve', 'Ano': 2012}
        
        if request.method == 'POST':
            if request.form.get('player'):
                players.append(request.form.get('player'))
                
        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)
    
    @app.route('/newGame', methods=["GET", "POST"])
    def newGame():
        nonlocal gamelist
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título':request.form.get('title'), 'Ano':request.form.get('year'), 'Categoria':request.form.get('category')})
            
        return render_template('newGame.html', gamelist=gamelist)
    
    @app.route('/apigames', methods = ['GET', 'POST'])
    @app.route('/apigames/<int:id>', methods = ['GET', 'POST'])
    def apigames(id = None):
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        gamesList = json.loads(data)
        #verificando se o parâmetro foi enviado
        if id:
            gameInfo = None
            for game in gamesList:
                if game['id'] == id:
                    gameInfo = game
                    break
            if gameInfo:
                return render_template('gameInfo.html', gameInfo = gameInfo)
            else:
                return f'Game com a id {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gamesList = gamesList)
        
         