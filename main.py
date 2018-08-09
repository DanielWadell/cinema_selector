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
        horror_movies_director = ['James Wan', 'Jennifer Kent', 'Oren Peli', 'Eduardo Sanchez', 'Jonathan Demme']
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
        action_movies_descriptions= ['Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal Johns prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance. Meanwhile, Iosefs father (Michael Nyqvist) -- Johns former colleague -- puts a huge bounty on Johns head.' , 'Police drama about a veteran officer who escorts a rookie on his first day with the LAPDs tough inner-city narcotics unit. "Training Day" is a blistering action drama that asks the audience to decide what is necessary, what is heroic and what crosses the line in the harrowing gray zone of fighting urban crime. Does law-abiding law enforcement come at the expense of justice and public safety? If so, do we demand safe streets at any cost?' , 'Bryan Mills (Liam Neeson), a former government operative, is trying to reconnect with his daughter, Kim (Maggie Grace). Then his worst fears become real when sex slavers abduct Kim and her friend shortly after they arrive in Paris for vacation. With just four days until Kim will be auctioned off, Bryan must call on every skill he learned in black ops to rescue her.', 'Disguised as a human, a cyborg assassin known as a Terminator (Arnold Schwarzenegger) travels from 2029 to 1984 to kill Sarah Connor (Linda Hamilton). Sent to protect Sarah is Kyle Reese (Michael Biehn), who divulges the coming of Skynet, an artificial intelligence system that will spark a nuclear holocaust. Sarah is targeted because Skynet knows that her unborn son will lead the fight against them. With the virtually unstoppable Terminator in hot pursuit, she and Kyle attempt to escape.' , 'Epic tale in which an intrepid archaeologist tries to beat a band of Nazis to a unique religious relic which is central to their plans for world domination. Battling against a snake phobia and a vengeful ex-girlfriend, Indiana Jones is in constant peril, making hairs-breadth escapes at every turn in this celebration of the innocent adventure movies of an earlier era.']
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
        mystery_movies_descriptions= ['The implausible escape of a brilliant murderess brings U.S. Marshal Teddy Daniels (Leonardo DiCaprio) and his new partner (Mark Ruffalo) to Ashecliffe Hospital, a fortress-like insane asylum located on a remote, windswept island. The woman appears to have vanished from a locked room, and there are hints of terrible deeds committed within the hospital walls. As the investigation deepens, Teddy realizes he will have to confront his own dark fears if he hopes to make it off the island alive.' ,'Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter peoples dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someones mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobbs every move.' , 'Leonard (Guy Pearce) is tracking down the man who raped and murdered his wife. The difficulty, however, of locating his wifes killer is compounded by the fact that he suffers from a rare, untreatable form of memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where hes going, or why.' , 'In the late 1960s and 1970s, fear grips the city of San Francisco as a serial killer called Zodiac stalks its residents. Investigators (Mark Ruffalo, Anthony Edwards) and reporters (Jake Gyllenhaal, Robert Downey Jr.) become obsessed with learning the killers identity and bringing him to justice. Meanwhile, Zodiac claims victim after victim and taunts the authorities with cryptic messages, cyphers and menacing phone calls.', 'When retiring police Detective William Somerset (Morgan Freeman) tackles a final case with the aid of newly transferred David Mills (Brad Pitt), they discover a number of elaborate and grizzly murders. They soon realize they are dealing with a serial killer (Kevin Spacey) who is targeting people he thinks represent one of the seven deadly sins. Somerset also befriends Mills wife, Tracy (Gwyneth Paltrow), who is pregnant and afraid to raise her child in the crime-riddled city.']
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