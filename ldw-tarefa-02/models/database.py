from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Criando a instância do SQLAlchemy
db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collection = db.Column(db.String(150))
    name = db.Column(db.String(150))
    category = db.Column(db.String(150))
    vps = db.Column(db.Integer)
    variant = db.Column(db.String(150))
    date = db.Column(db.Date)
    
    # Método construtor da classe
    def __init__(self, collection, name, category, vps, variant, date):
        self.collection = collection
        self.name = name
        self.category = category
        self.vps = vps
        self.variant = variant
        # Converter string para date se necessário
        if isinstance(date, str):
            try:
                # Tentar formato brasileiro primeiro (dd/mm/aaaa)
                if '/' in date:
                    self.date = datetime.strptime(date, '%d/%m/%Y').date()
                # Tentar formato ISO (aaaa-mm-dd)
                elif '-' in date:
                    self.date = datetime.strptime(date, '%Y-%m-%d').date()
                else:
                    raise ValueError(f"Formato de data não reconhecido: {date}")
            except ValueError as e:
                print(f"Erro ao converter data '{date}': {e}")
                self.date = None
        else:
            self.date = date