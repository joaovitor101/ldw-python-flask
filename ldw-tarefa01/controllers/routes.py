from flask import render_template, request


def init_app(app):
     agentes = ['Jett', 'Sova', 'Sage']
     armas = [
         {'Nome': 'Vandal', 'Categoria': 'Rifle', 'Preço': 2900},
     ]
     mapas = ['Ascent', 'Bind', 'Haven']

     @app.route('/')
     def home():
         return render_template('index.html')

     # Rota com inclusão e exibição via lista (Agentes)
     @app.route('/agentes', methods=["GET", "POST"]) 
     def agentes_view():
         nonlocal agentes
         if request.method == 'POST':
             novo_agente = request.form.get('agente')
             if novo_agente:
                 agentes.append(novo_agente)
         return render_template('agentes.html', agentes=agentes)

     # Rota com inclusão via dicionário e exibição em tabela (Armas)
     @app.route('/armas', methods=["GET", "POST"]) 
     def armas_view():
         nonlocal armas
         if request.method == 'POST':
             nome = request.form.get('name')
             categoria = request.form.get('category')
             preco = request.form.get('price')
             if nome and categoria and preco:
                 armas.append({'Nome': nome, 'Categoria': categoria, 'Preço': int(preco)})
         return render_template('armas.html', armas=armas)

     # Nova rota extra (Mapas) com inclusão via lista
     @app.route('/mapas', methods=["GET", "POST"]) 
     def mapas_view():
         nonlocal mapas
         if request.method == 'POST':
             novo_mapa = request.form.get('mapa')
             if novo_mapa:
                 mapas.append(novo_mapa)
         return render_template('mapas.html', mapas=mapas)

