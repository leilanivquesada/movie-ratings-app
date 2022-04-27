"""CRUD Operations"""

from model import db, User, Movie, Ratings, connect_to_db
 
if __name__ == '__main__':
     from server import app
     connect_to_db(app)
     
     
def create_user(email,password):
    user = User(email=email, password=password)
    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""
    new_movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    return new_movie

def create_rating(score, user_id, movie_id):
    """Create and return new rating."""
    rating = Ratings(score=score, user_id=user_id, movie_id=movie_id)
    return rating