from flask import Flask, render_template
from app.api.routes.movie_routes import movie_router

app = Flask(__name__)
app.register_blueprint(movie_router, url_prefix='/api')

# Añade esta nueva ruta raíz
@app.route('/')
def index():
    """Sirve la página principal de la aplicación web."""
    return render_template('index.html')
