'''
Created on Aug 31, 2015

@author: jhamilton
'''

import tornado.web
import aries

class TestHandler(tornado.web.RequestHandler):
    ''' Defines the main application controller 
    
    '''
    def initialize(self):
        self.app = aries.core.Aries() 
    
    def get(self):
        ''' Called when the application recieves a get request to home
        
        Renders the test.html template, passing a JSON representation of
        the Aries instance to the template.
        '''
        
        self.write("Aries")

ARIES_COUPLING = [
    (r"/aries", TestHandler)
]    