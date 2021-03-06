#!/usr/bin/env python
# coding: utf-8

# In[2]:



import unittest
from padaku.perinfo import age as a


class TestAge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class")
    
    def setUp(self):
        print("Set Up")
    
    def test_age(self):    
        
        self.assertMultiLineEqual(a.age("1996-3-15"),"The age of the person is 22 years")
        self.assertMultiLineEqual(a.age("1959-3-12"),"The age of the person is 59 years")
        self.assertMultiLineEqual(a.age("1932-1-1"),"The age of the person is 87 years")
        self.assertMultiLineEqual(a.age("1962-02-02"),"The age of the person is 56 years")
        self.assertMultiLineEqual(a.age("1976-07-06"),"The age of the person is 42 years")
        self.assertMultiLineEqual(a.age("1976-07-06"),"The age of the person is 42 years")
        
    
    def tearDown(self):
        print("Tear Down")
    
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")
        
unittest.main(argv=[''],verbosity=2,exit=False)