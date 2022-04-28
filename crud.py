"""CRUD Operations"""

from model import db, User, Movie, Ratings, connect_to_db
 
if __name__ == '__main__':
     from server import app
     connect_to_db(app)
     
     
def create_user(email,password):
    user = User(email=email, password=password)
    return user

def get_users():
    """Return all users"""
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    new_movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    return new_movie

def get_movies():
    """Return all movies"""
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)

def create_rating(score, user_id, movie_id):
    """Create and return new rating."""
    rating = Ratings(score=score, user_id=user_id, movie_id=movie_id)
    return rating