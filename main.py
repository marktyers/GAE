import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('App Pushed from GitHub')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
