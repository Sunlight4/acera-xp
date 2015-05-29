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
        self.response.write('''<html>
        <head>
        <script type="text/javascript" src="pjs/processing.js"></script>
        <script type="text/javascript">
        function load() {
        var pjs = Processing.getInstanceById("visual");
        var xml = $.get("http://thatfunkysite.com/serving/getxml.php");
        pjs.buildFromXML(xml);
        }
        </script>
        <title>Acera MS XP System</title>
        </head>
        <body onload="load()">
        <canvas data-processing-sources="pjs/pjs.pde" id="visual"></canvas>
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
class XMLHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><xml>')
        students=Student.query().fetch(100)
        for student in students:
            self.response.write("<student name='"+student.name+"' email='"+student.user.email()+"' xp='"+str(student.xp)+"'  multiplier='"
                                +str(student.multiplier)
                                +"'></student>")
        self.response.write("</xml>")
app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/init', InitHandler), ('/xml', XMLHandler)
], debug=True)
