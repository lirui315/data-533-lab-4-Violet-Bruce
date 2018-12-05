#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
from padaku.perinfo import age as a


# In[17]:


class TestAge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class")
    
    def setUp(self):
        print("Set Up")
    
    def test_age(self):    
        
        self.assertMultiLineEqual(a.age("1996-3-15"),"The age of the person is 22 and 268 days")
        self.assertMultiLineEqual(a.age("1959-3-12"),"The age of the person is 59 and 281 days")
        self.assertMultiLineEqual(a.age("1932-1-1"),"The age of the person is 86 and 358 days")
        self.assertMultiLineEqual(a.age("1962-02-02"),"The age of the person is 56 and 318 days")
        self.assertMultiLineEqual(a.age("1976-07-06"),"The age of the person is 42 and 160 days")
    
    def tearDown(self):
        print("Tear Down")
    
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")
        
unittest.main(argv=[''],verbosity=2,exit=False)

