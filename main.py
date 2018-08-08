import webapp2
from random import shuffle
import jinja2
import os
from random import shuffle


#libraries for APIs
from google.appengine.api import urlfetch
import json


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
        about_template = the_jinja_env.get_template('templates/comedy.html')
        comedy_movies = ['https://www.youtube.com/embed/cd-go0oBF4Y','https://www.youtube.com/embed/CXqxP-bUC7I',
        'https://www.youtube.com/embed/l13yPhimE3o','https://www.youtube.com/embed/D6gABQFR94U','https://www.youtube.com/embed/MNpoTxeydiY']
        shuffle(comedy_movies)
        movie_pick = comedy_movies[0]
        comedy_dict = {
            'movie_trailer': movie_pick
        }
        self.response.write(about_template.render(comedy_dict))
    
class Drama(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/comedy.html')
        drama_movies = ['https://www.youtube.com/embed/lB95KLmpLR4','https://www.youtube.com/embed/5gcyB72nFmc',
        'https://www.youtube.com/embed/89Kq8SDyvfg','https://www.youtube.com/embed/6hB3S9bIaco','https://www.youtube.com/embed/M5FpB6qDGAE']
        shuffle(drama_movies)
        movie_pick = drama_movies[0]
        drama_dict = {
            'movie_trailer': movie_pick
        }
        self.response.write(about_template.render(drama_dict))



    

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/comedy', Comedy)
], debug=True)