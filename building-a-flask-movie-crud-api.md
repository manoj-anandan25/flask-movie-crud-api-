 Building a Movie CRUD API with Flask & SQLite (Beginner-Friendly Guide)

 Introduction

Ever wanted to build your own movie database where you can **add, view, update, and delete** your favorite films?
In this guide, we’ll walk through creating a **Movie CRUD API** using **Flask** and **SQLite** — a perfect starting point for learning REST APIs.

By the end, you’ll have:

* A working Flask API
* Full CRUD operations
* SQLite as your database
* Postman or PowerShell commands to test it

---

 Tech Stack

* Python
* Flask — Web framework
* Flask-SQLAlchemy — ORM for database management
* SQLite — Lightweight database

---

 Project Structure

```
flask-movie-crud-api/
│
├── app.py               # Main Flask app
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

 Step 1 — Install Dependencies

Create a virtual environment and install required packages.

```bash
pip install flask flask_sqlalchemy
```

---

 Step 2 — The Flask Application

Here’s the complete `app.py` code:

```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<MOVIE: {self.title}-{self.director}-{self.rating}-{self.year}>"

# Home route
@app.route('/')
def home():
    return 'Hello there!'

# Get all movies
@app.route('/movies')
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
    return {"Movies": output}

# Get movie by ID
@app.route('/movies/<id>')
def get_movie(id):
    movie = Movie.query.get(id)
    return {
        "title": movie.title,
        "director": movie.director,
        "rating": movie.rating,
        "year": movie.year
    }

# Add movie
@app.route('/movies', methods=['POST'])
def add_movie():
    movie = Movie(
        title=request.json['title'],
        director=request.json['director'],
        rating=request.json['rating'],
        year=request.json['year']
    )
    db.session.add(movie)
    db.session.commit()
    return {"id": movie.id}

# Update movie (PUT)
@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not found"}
    movie.title = request.json['title']
    movie.director = request.json['director']
    movie.rating = request.json['rating']
    movie.year = request.json['year']
    db.session.commit()
    return {"message": "Updated Successfully", "id": movie.id}

# Partial update (PATCH)
@app.route('/movies/<id>', methods=['PATCH'])
def patch_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not found"}
    if "title" in request.json:
        movie.title = request.json['title']
    if "director" in request.json:
        movie.director = request.json['director']
    if "rating" in request.json:
        movie.rating = request.json['rating']
    if "year" in request.json:
        movie.year = request.json['year']
    db.session.commit()
    return {"message": "Patched Successfully", "id": movie.id}

# Delete movie
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if movie is None:
        return {"error": "Not Found"}
    db.session.delete(movie)
    db.session.commit()
    return {"message": "Deleted Successfully"}

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

---

 Step 3 — Running the App

```bash
python app.py
```

By default, your API runs at:

```
http://127.0.0.1:5000
```

---

 Step 4 — Testing the API

### Using Postman

You can easily test:

* GET `/movies`
* GET `/movies/<id>`
* POST `/movies`
* PUT `/movies/<id>`
* PATCH `/movies/<id>`
* DELETE `/movies/<id>`

---

 Using PowerShell

Example: Add a new movie

```powershell
$NewMovie = @{
    title    = "Inception"
    director = "Christopher Nolan"
    rating   = 8.8
    year     = 2010
}
Invoke-RestMethod -Uri "http://127.0.0.1:5000/movies" `
    -Method POST `
    -Body ($NewMovie | ConvertTo-Json) `
    -ContentType "application/json"
```

---

Conclusion

We’ve built a fully functional CRUD API using Flask and SQLite — perfect for beginners learning REST concepts.
You can now:

* Host it on Heroku or PythonAnywhere
* Replace SQLite with MySQL/PostgreSQL
* Add authentication for security

If you found this useful, ⭐ star the GitHub repo and share it with your friends.

---

