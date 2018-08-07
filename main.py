import webapp2
from random import shuffle
import jinja2
import os
from models import Movie

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
   


class Results(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(about_template.render())
        results_template = the_jinja_env.get_template('templates/results.html')
        comedy_choice = self.request.get('user-comedy-choice')
        mystery_choice = self.request.get('user-mystery-choice')
        action_choice = self.request.get('user-action-choice')
        drama_choice = self.request.get('user-drama-choice')
        horror_choice = self.request.get('user-horror-choice')
        
        movie_dict = {
            'action': 'https://www.youtube.com/watch?v=gKTVQPOH8ZA',
            
        }
        
        


    

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/results', Results)
], debug=True)