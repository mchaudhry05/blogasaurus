#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import os
import jinja2

#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('my_blog.html')
        self.response.write(template.render())
class LinksHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        template2 = jinja_current_directory.get_template('links.html')
        self.response.write(template2.render())
class PostsHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        template3 = jinja_current_directory.get_template('posts.html')
        self.response.write(template3.render())
class AboutMeHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        template4 = jinja_current_directory.get_template('about_me.html')
        self.response.write(template4.render())
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/links', LinksHandler),
    ('/posts', PostsHandler),
    ('/about_me', AboutMeHandler),
], debug=True)
