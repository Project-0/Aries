'''
Sets up an Aries Tornado server configured for debug and testing

# Development Server

This application is intended to provide an interface that developers can ping 
to perfrom tests.

Run with `$ python bin dev_server`

Created on Aug 20, 2015

@author: jhamilton
'''
import os

from aries.core import Aries
import aries_coupler
import tornado
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index.html')

# Initialize the server object from the coupling definition
client_app = (r'/', IndexHandler)
controllers = [aries_coupler.ARIES_COUPLING[0], client_app]

settings = {'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static")
            }

server = tornado.web.Application(controllers, **settings)


def dev_main():
    print "starting server..."
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    

if __name__ == '__main__':
    dev_main()