from google.appengine.ext import ndb

class Movie(ndb.Model):
    comedy_choice = ndb.StringProperty(required=True)
    mystery_choice = ndb.StringProperty(required=True)
    action_choice = ndb.StringProperty(required=True)
    drama_choice = ndb.StringProperty(required=True)
    horror_choice = ndb.StringProperty(required=True)
    