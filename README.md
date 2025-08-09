
 Flask Movie CRUD API

A simple REST API built with Flask and Flask-SQLAlchemy to manage a movie collection.  
Supports full CRUD operations (Create, Read, Update, Delete) and partial updates.  
Tested with Postman — collection included.

---

 Features
- Get all movies or a single movie
- Add new movies
- Update movies (full update with PUT, partial update with PATCH)
- Delete movies
- SQLite database for easy setup

---

 Tech Stack
- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (default DB)

---

 Project Structure
```

flask-movie-crud-api/
│
├── app.py                                  # Main Flask app with endpoints
├── requirements.txt                        # Dependencies
├── Flask Movie API.postman\_collection.json # Postman collection (optional)
└── README.md                               # Documentation

````

---

 Getting Started

 Clone the repository
```bash
git clone https://github.com/<your-username>/flask-movie-crud-api.git
cd flask-movie-crud-api
````

Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

 Install dependencies

```bash
pip install -r requirements.txt
```

Initialize the database

In Python shell:

```python
from app import db
db.create_all()
```

Run the application

```bash
python app.py
```

API will run on:
📍 `http://127.0.0.1:5000`

---

 API Endpoints

| Method | Endpoint       | Description            | Request Body (JSON)                                            |
| ------ | -------------- | ---------------------- | -------------------------------------------------------------- |
| GET    | `/`            | Hello test message     | None                                                           |
| GET    | `/movies`      | Get all movies         | None                                                           |
| GET    | `/movies/<id>` | Get a movie by ID      | None                                                           |
| POST   | `/movies`      | Add a new movie        | `{ "title": "", "director": "", "rating": 0.0, "year": 2024 }` |
| PUT    | `/movies/<id>` | Full update a movie    | `{ "title": "", "director": "", "rating": 0.0, "year": 2024 }` |
| PATCH  | `/movies/<id>` | Partial update a movie | Any of the movie fields                                        |
| DELETE | `/movies/<id>` | Delete a movie by ID   | None                                                           |

---

 Testing with Postman

1. Open **Postman**
2. Import `Flask Movie API.postman_collection.json` (if included)
3. Test each endpoint:

   * GET all movies
   * GET movie by ID
   * POST new movie
   * PUT update movie
   * PATCH update part of movie
   * DELETE movie

 Watch on YouTube  
I’ve made a beginner-friendly tutorial video for this project.  
👉 [**Watch here on YouTube**](https://youtu.be/VPd1e3xfCHg)  




