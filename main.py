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
        filter = self.request.get('filter')
        base_url = 'https://ghibliapi.herokuapp.com/{}'.format(filter)
        response = json.loads(urlfetch.fetch(base_url).content)
        template = jinja_env.get_template('templates/results.html')
        self.response.write(template.render({'response':response}))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/search', SearchHandler)
    ], debug=True)
