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
    
def run_query(first_line, second_line, pic_type):
    movie_choices = Movie(line1=first_line, line2 = second_line, img_choice = pic_type)
    movie_key = movie_choices.put()
    print movie_key

    
class Welcome(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(about_template.render())
   


class Results(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(about_template.render())
    
class MovieHandler(webapp2.RequestHandler):
    def get(self): 
        results_template = the_jinja_env.get_template('templates/results.html')
        comedy_choice = self.request.get('user-comedy-choice')
        mystery_choice = self.request.get('user-mystery-choice')
        action_choice = self.request.get('user-action-choice')
        drama_choice = self.request.get('user-drama-choice')
        horror_choice = self.request.get('user-horror-choice')
    

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/results', Results)
], debug=True)