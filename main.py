import webapp2
from random import shuffle
import jinja2
import os
from random import randint




the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    


    
class Welcome(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())
        
    
        
   
class Comedy(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/comedy.html')
        comedy_movies = ['https://www.youtube.com/embed/cd-go0oBF4Y','https://www.youtube.com/embed/CXqxP-bUC7I',
        'https://www.youtube.com/embed/l13yPhimE3o','https://www.youtube.com/embed/D6gABQFR94U','https://www.youtube.com/embed/MNpoTxeydiY']
        comedy_movies_title = ['The Big Lebowski','Meet the Parents','Dumb and Dumber','Ferris Buellers Day Off','SuperBad']
        comedy_movies_director = ['Ethan and Joel Cohen', 'Jay Roach', 'Peter Farrelly', 'John Hughes', 'Greg Mottola']
        movie_pick = comedy_movies[spot]
        movie_title_pick = comedy_movies_title[spot]
        movie_director = comedy_movies_director[spot]
        comedy_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
        }
        self.response.write(about_template.render(comedy_dict))
    
class Drama(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/drama.html')
        drama_movies = ['https://www.youtube.com/embed/lB95KLmpLR4','https://www.youtube.com/embed/5gcyB72nFmc',
        'https://www.youtube.com/embed/89Kq8SDyvfg','https://www.youtube.com/embed/6hB3S9bIaco','https://www.youtube.com/embed/M5FpB6qDGAE']
        drama_movies_title = ['The Social Network','The Imitation Game','The Pursuit of Happyness','The Shawshank Redemption','Schindlers List']
        drama_movies_director = ['David Fincher', 'Morten Tyldum', 'Gabriele Muccino', 'Frank Darabont', 'Steven Spielberg']
        movie_pick = drama_movies[spot]
        movie_title_pick = drama_movies_title[spot]
        movie_director = drama_movies_director[spot]
        drama_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
        }
        self.response.write(about_template.render(drama_dict))

class Horror(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/horror.html')
        horror_movies = ['https://www.youtube.com/embed/k10ETZ41q5o','https://www.youtube.com/embed/k5WQZzDRVtw',
        'https://www.youtube.com/embed/F_UxLEqd074','https://www.youtube.com/embed/a_Hw4bAUj8A','https://www.youtube.com/embed/lQKs169Sl0I']
        horror_movies_title = ['The Conjuring','The Babadook','Paranormal Activity','The Blair Witch Project','The Silence of the Lambs']
        horror_movies_director = ['James Wan', 'Jennifer Kent', 'Oren Peli', 'Eduardo Sánchez', 'Jonathan Demme']
        movie_pick = horror_movies[spot]
        movie_title_pick = horror_movies_title[spot]
        movie_director = horror_movies_director[spot]
        horror_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
        }
        self.response.write(about_template.render(horror_dict))

class Action(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/action.html')
        action_movies = ['https://www.youtube.com/embed/bvaftiAu7mw','https://www.youtube.com/embed/gKTVQPOH8ZA',
        'https://www.youtube.com/embed/pbA-tBrHNfI','https://www.youtube.com/embed/c4Jo8QoOTQ4','https://www.youtube.com/embed/0ZOcoxjeUYo']
        action_movies_title = ['John Wick','Training Day','Taken','The Terminator','Raiders of the Lost Ark']
        action_movies_director = ['Chad Stahelski', 'Antoine Fuqua', 'Pierre Morel', 'James Cameron', 'Steven Spielberg']
        movie_pick = action_movies[spot]
        movie_title_pick = action_movies_title[spot]
        movie_director = action_movies_director[spot]
        action_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
        }
        self.response.write(about_template.render(action_dict))
    
class Mystery(webapp2.RequestHandler):
    def get(self):
        spot = randint(0,4)
        about_template = the_jinja_env.get_template('templates/mystery.html')
        mystery_movies = ['https://www.youtube.com/embed/5iaYLCiq5RM','https://www.youtube.com/embed/66TuSJo4dZM',
        'https://www.youtube.com/embed/0vS0E9bBSL0','https://www.youtube.com/embed/bEvnwKFUnI0','https://www.youtube.com/embed/J4YV2_TcCoE']
        mystery_movies_title = ['Shutter Island','Inception','Memento','Zodiac','Se7en']
        mystery_movies_director = ['Martin Scorsese', 'Christopher Nolan', 'Christopher Nolan', 'David Fincher', 'David Fincher']
        movie_pick = mystery_movies[spot]
        movie_title_pick = mystery_movies_title[spot]
        movie_director = mystery_movies_director[spot]
        mystery_dict = {
            'movie_trailer': movie_pick,
            'movie_title': movie_title_pick,
            'movie_director': movie_director
            
           # 'movie-description': 
        }
        self.response.write(about_template.render(mystery_dict))
        
        
app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/comedy', Comedy),
    ('/drama', Drama),
    ('/horror', Horror),
    ('/action', Action),
    ('/mystery', Mystery)
], debug=True)