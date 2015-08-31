'''
Created on Aug 20, 2015

@author: jhamilton
'''
import unittest
import aries
from bin import dev_server


class TestDevServerMain(unittest.TestCase):


    def test_Name(self):
        app = dev_server.dev_main()
        self.assertIsInstance(app, aries.core.Aries)


def TestDevServerSuite():
    TestDevServerSuite = unittest.TestSuite()
    TestDevServerSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDevServerMain))
    return TestDevServerSuite