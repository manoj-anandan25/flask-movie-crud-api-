"""
Flask Movie API
---------------
A simple CRUD API to manage movies using Flask and SQLAlchemy.

Endpoints:
    GET    /movies            - Get all movies
    GET    /movies/<id>       - Get a specific movie by ID
    POST   /movies            - Add a new movie
    PUT    /movies/<id>       - Update all fields of a movie
    PATCH  /movies/<id>       - Update some fields of a movie
    DELETE /movies/<id>       - Delete a movie by ID
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Database configuration (SQLite file stored locally)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Movie model (database table)
class Movie(db.Model):
    """
    Movie database model with:
    - title (string)
    - director (string)
    - rating (float)
    - year (integer)
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<MOVIE: {self.title} - {self.director} - {self.rating} - {self.year}>"

# Default home route
@app.route('/')
def home():
    return 'Hello there! Welcome to the Movie API 🎬'

# GET: Fetch a specific movie by ID
@app.route('/movies/<id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Movie not found"}, 404
    return {
        "title": movie.title,
        "director": movie.director,
        "rating": movie.rating,
        "year": movie.year
    }

# GET: Fetch all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    output = []
    for movie in movies:
        movie_data = {
            "title": movie.title,
            "director": movie.director,
            "rating": movie.rating,
            "year": movie.year
        }
        output.append(movie_data)
    return {"movies": output}

# POST: Add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    movie = Movie(
        title=data['title'],
        director=data['director'],
        rating=data['rating'],
        year=data['year']
    )
    db.session.add(movie)
    db.session.commit()
    return {"id": movie.id}, 201

# DELETE: Remove a movie by ID
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not Found"}, 404
    db.session.delete(movie)
    db.session.commit()
    return {"message": "Movie deleted successfully!"}

# PUT: Fully update a movie
@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not found"}, 404
    data = request.json
    movie.title = data['title']
    movie.director = data['director']
    movie.rating = data['rating']
    movie.year = data['year']
    db.session.commit()
    return {"message": "Updated successfully", "id": movie.id}

# PATCH: Partially update a movie
@app.route('/movies/<id>', methods=['PATCH'])
def patch_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not found"}, 404
    data = request.json
    if "title" in data:
        movie.title = data['title']
    if "director" in data:
        movie.director = data['director']
    if "rating" in data:
        movie.rating = data['rating']
    if "year" in data:
        movie.year = data['year']
    db.session.commit()
    return {"message": "Patched successfully", "id": movie.id}


