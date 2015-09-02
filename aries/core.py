'''
Created on Jul 27, 2015

@author: jhamilton
'''

import json

class Aries(object):
    """ Defines the root object 
    """
    
    def __init__(self, journal_path="~/Documents/"):
        self.journal_path = journal_path
        print self.journal_path
        
    def __repr__(self):
        json_dump = json.dumps(dict({
            'journal_path': self.journal_path
        })) 
        return json_dump