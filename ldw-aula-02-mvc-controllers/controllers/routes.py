from flask import render_template, request, redirect, url_for

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