# app.py
from flask import Flask
from config import Config
from models import db
from routes import app_bp  # Importe le blueprint des routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation de la base de données
    db.init_app(app)

    # Enregistrement du blueprint des routes
    app.register_blueprint(app_bp) # Enregistre le blueprint

    return app


app = create_app() # Création de l'application

# Création des tables de la base de données (à faire dans un contexte d'application)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) # Ne pas utiliser debug=True en production