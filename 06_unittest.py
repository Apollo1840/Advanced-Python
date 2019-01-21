# -*- coding: utf-8 -*-

import unittest

import sys
import os
sys.path.append(os.getcwd()+'\\tools')
from plus_substract import plus, substract


class simpleTestCase(unittest.TestCase):
    
    def test_sub(self):
        self.assertEqual(substract(2,2),0)
        self.assertEqual(substract(2,1),1)
        
        with self.assertRaise(TypeError):
            substract(1,'b')
    

# setUp and tearDown
class DummyTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):  # do it once before test
        print('preparation')
    
    @classmethod
    def tearDownClass(self):# do it once aftertest
        print('end')
    
    def setUp(self):  # do it every time before test
        print('set up the data')
    
    def tearDown(self):# do it every time aftertest
        print('tear down the files')
        
    
    def test_add(self):
        self.assertEqual(plus(1,2),3)
        self.assertEqual(plus(1,1),2)
        self.assertEqual(plus('a','b'),'ab')

    def test_sub(self):
        self.assertEqual(substract(2,2),0)
        self.assertEqual(substract(2,1),1)
        
        with self.assertRaise(TypeError):
            substract(1,'b')
        
if __name__ == '__main__':
    unittest.main()
    
    
# you can use mock (path) in unitest to separate your code to enviroment.
# see: https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=21
        