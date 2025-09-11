from flask import render_template, request, redirect, url_for
import urllib
import json
from models.database import Game,db

def init_app(app):
    # Lista de agentes (para exibição em lista)
    agents = ['Jett', 'Phoenix', 'Sage', 'Omen', 'Reyna']
    gamelist = [{'Título': 'CS 1.6', 'Ano': 1996, 'Categoria': 'FPS Online'}]
    # Lista de mapas (para exibição em tabela)
    maps = [{'Nome': 'Ascent', 'Tipo': 'Bomb', 'Região': 'Itália', 'Lancamento': '2020'}]
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/agents', methods=["GET", "POST"])
    def agents_page():
        nonlocal agents
        title = 'Valorant'
        year = 2020
        category = 'FPS Tático'
        
        game_info = {'Nome': 'Valorant', 'Desenvolvedor': 'Riot Games', 'Ano': 2020}
        
        if request.method == 'POST':
            if request.form.get('agent'):
                agents.append(request.form.get('agent'))
                
        return render_template('agents.html', title=title, year=year, category=category, agents=agents, game_info=game_info)
    
    @app.route('/maps', methods=["GET", "POST"])
    def maps_page():
        nonlocal maps
        if request.method == 'POST':
            if request.form.get('name') and request.form.get('type') and request.form.get('region') and request.form.get('release'):
                maps.append({
                    'Nome': request.form.get('name'), 
                    'Tipo': request.form.get('type'), 
                    'Região': request.form.get('region'), 
                    'Lancamento': request.form.get('release')
                })
            
        return render_template('maps.html', maps=maps) 

    
    @app.route('/newgame', methods=['GET', 'POST'])
    def newgame():

        # Tratando a requisição a POST
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título': request.form.get('title'), 'Ano': request.form.get(
                    'year'), 'Categoria': request.form.get('category')})
                return redirect(url_for('newgame'))

        return render_template('newGame.html', gamelist=gamelist)
    
    @app.route('/apigames', methods=['GET', 'POST'])
    @app.route('/apigames/<id>', methods=['GET', 'POST'])
    def apigames(id=None):  # Lista agentes de Valorant e detalhe por UUID
        if id:
            # Detalhe do agente por UUID
            url = f'https://valorant-api.com/v1/agents/{id}'
            response = urllib.request.urlopen(url)
            data = response.read()
            payload = json.loads(data)
            if payload.get('status') == 200 and payload.get('data'):
                gameInfo = payload['data']
                return render_template('gameinfo.html', gameInfo=gameInfo)
            return f'Agente com UUID {id} não encontrado.'
        else:
            # Lista de agentes jogáveis
            url = 'https://valorant-api.com/v1/agents?isPlayableCharacter=true'
            response = urllib.request.urlopen(url)
            data = response.read()
            payload = json.loads(data)
            gamesList = payload.get('data', [])
            return render_template('apigames.html', gamesList=gamesList)

    @app.route('/estoque', methods=['GET', 'POST'])
    def estoque():
        if request.method == 'POST':
            newGame = Game(request.form['collection'], request.form['name'], request.form['category'],
                           request.form['vps'], request.form['variant'], request.form['data'])
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque'))
        gameEstoque = Game.query.all()
        return render_template('estoque.html', gameEstoque=gameEstoque)
    
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        game = Game.query.get(id)
        if request.method == 'POST':
            game.title = request.form['title']
            game.year = request.form['year']
            game.category = request.form['category']
            game.platform = request.form['platform']
            game.price = request.form['price']
            game.quantity = request.form['quantity']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editgame.html', game=game)
    
    @app.route('/estoque/delete/<int:id>')
    def delete_estoque(id):
        game = Game.query.filter_by(id=id).first()
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('estoque'))