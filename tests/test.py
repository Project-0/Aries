'''
Created on Aug 20, 2015

@author: jhamilton
'''
import unittest
import test_dev_server

dev_server = test_dev_server.TestDevServerSuite()
alltests = unittest.TestSuite([dev_server])

unittest.TextTestRunner(verbosity=2).run(alltests)