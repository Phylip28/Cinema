from flask import Flask
from app.api.routes.movie_routes import movie_router

app = Flask(__name__)

# Registramos nuestro blueprint de rutas en la aplicación principal
# con un prefijo /api
app.register_blueprint(movie_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)