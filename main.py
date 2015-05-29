#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users, mail, images
from google.appengine.ext import ndb, db
import webapp2, random, pickle, urllib, datetime, locale
locale.setlocale(locale.LC_ALL, '')
class Student(ndb.Model):
    xp=ndb.IntegerProperty()
    multiplier=ndb.IntegerProperty()
    name=ndb.StringProperty()
    user=ndb.UserProperty()
class MainHandler(webapp2.RequestHandler):
    def get(self):
        f=open("pde/update.txt", "w")
        s=Student.fetch(100)
        for student in s:
            f.write(student.name+"::"+str(student.xp)+"::"+str(student.multiplier)+"::"+student.user.email()+"\n")
        f.close()
        self.response.write('''<html>
        <head>
        <script type="text/javascript" src="pjs/processing.js"></script>
        <title>Acera MS XP System</title>
        </head>
        <body>
        <canvas data-processing-sources="pjs/pjs.pde"></canvas>
        </body>
        </html>''')
class InitHandler(webapp2.RequestHandler):
    def get(self):
        ethan=Student()
        ethan.xp=128
        ethan.multiplier=1
        ethan.name="Ethan"
        ethan.user=users.User("ethans@aceraschool.org")
        ethan.put()
        theo=Student()
        theo.xp=124
        theo.multiplier=2
        theo.name="Theo"
        theo.user=users.User("theoh@aceraschool.org")
        theo.put()
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/init', InitHandler)
], debug=True)
