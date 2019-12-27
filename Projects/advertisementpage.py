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
import datetime
import meme_model

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MememMainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        data = {
        'greeting':'seetow',
        'adjective':'amazing',
        }
        self.response.write(start_template.render(data))

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = jinja_current_dir.get_template('templates/results.html')
        self.response.write(welcome_template.render())
    def post(self):
        results_template = jinja_current_dir.get_template('templates/results.html')
        meme_line1 = self.request.get("user-first-ln")
        meme_line2 = self.request.get("user-second-ln")
        meme_choice = self.request.get("meme-type")
        print(meme_line1, type(meme_line1))
        if meme_choice == 'college-grad':
            url = "https://cdn.wccftech.com/wp-content/uploads/2019/06/WCCFcyberpunk20779.jpg"
        elif meme_choice == 'thinking-ape':
            url = "https://cdn.wccftech.com/wp-content/uploads/2019/06/WCCFcyberpunk20779.jpg"
        elif meme_choice == 'coding':
            url = "https://cdn.wccftech.com/wp-content/uploads/2019/06/WCCFcyberpunk20779.jpg"
        else:
            url = "https://cdn.wccftech.com/wp-content/uploads/2019/06/WCCFcyberpunk20779.jpg"
        author = self.request.get("usr")
        date = str(datetime.datetime.now())
        user_info = {
        "line1":meme_line1,
        "line2":meme_line2,
        "img_url": url,
        "author": author,
        "date": date
        }
        meme = meme_model.Meme(
        top_line = meme_line1,
        bottom_line = meme_line2,
        date = date,
        author = author,
        image_option = url
        )
        meme.put()
        self.response.write(results_template.render(user_info))

class ShowLibrary(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_current_dir.get_template('templates/library.html')

        meme_query = meme_model.Meme.query().fetch()

        template_vars = {
        'memes':meme_query
        }
        self.response.write(result_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MememMainHandler),
    ('/result', EnterInfoHandler),
    ('/library', ShowLibrary)
], debug=True)
