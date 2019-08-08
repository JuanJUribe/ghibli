import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
from urllib import urlencode

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render())

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        # ingredients = self.request.get('ingredients')
        # recipe = self.request.get('recipe')
        base_url = 'http:/ghibli.herokuapp.com/films'
        # params = {
        #     'i':ingredients,
        #      'q':recipe
        # }
        # response = urlfetch.fetch(base_url+urlencode(params)).content
        # results = json.loads(response)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render())

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler)
    ], debug=True)
