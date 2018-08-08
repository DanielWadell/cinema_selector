import webapp2
from random import shuffle
import jinja2
import os

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
        comedy_movies = ['https://www.youtube.com/embed/cd-go0oBF4Y']
        movie_pick = comedy_movies[0]
        
        comedy_dict = {
            'movie_trailer': 'https://www.youtube.com/embed/cd-go0oBF4Y'
        }
        self.response.write(about_template.render(comedy_dict))
    




    

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/comedy', Comedy)
], debug=True)