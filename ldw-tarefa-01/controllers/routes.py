from flask import render_template, request, redirect, url_for

def init_app(app):
    # Lista de agentes (para exibição em lista)
    agents = ['Jett', 'Phoenix', 'Sage', 'Omen', 'Reyna']
    
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