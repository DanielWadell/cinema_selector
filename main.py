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
            'comedy-movie': 'https://www.youtube.com/watch?v=ayTnvVpj9t4',
            'action-movie': 'https://www.youtube.com/watch?v=gKTVQPOH8ZA',
            'mystery-movie': 'https://www.youtube.com/watch?v=66TuSJo4dZM',
            'drama-movie': 'https://www.youtube.com/watch?v=7d_jQycdQGo',
            'horror-movie': 'https://www.youtube.com/watch?v=E1YbOMDI59k'
            
        }
        
        if comedy_choice == True:
            self.response.write(results_template.render(movie_dict['comedy-movie']))
        elif mystery_choice == True:
            self.response.write(results_template.render(movie_dict['mystery-movie']))
        elif action_choice == True:
            self.response.write(results_template.render(movie_dict['action-movie']))
        elif drama_choice == True:
            self.response.write(results_template.render(movie_dict['drama-movie']))
        elif horror_choice == True:
            self.response.write(results_template.render(movie_dict['horror-movie']))
        


    

app = webapp2.WSGIApplication([
    ('/', Welcome),
    ('/results', Results)
], debug=True)