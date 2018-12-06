
# coding: utf-8

# In[1]:


import unittest
from padaku.birth import number


# In[2]:


class TestNumber(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    def setUp(self):
        print('Set Up')
    
    def test_birthdate(self):
        self.assertMultiLineEqual(number.life_path_number(1996,3,15),"Your life path number is 7")
        self.assertMultiLineEqual(number.life_path_number(1990,10,25),"Your life path number is 9")
        self.assertMultiLineEqual(number.life_path_number(1994,4,21),"Your life path number is 3")
        self.assertMultiLineEqual(number.life_path_number(1995,11,6),"Your life path number is 5")
        self.assertMultiLineEqual(number.life_path_number(1991,12,27),"Your life path number is 5")       

    def tearDown(self):
        print('Tear Down')
    
    @classmethod    
    def tearDownClass(cls):
        print('teardownClass') 
unittest.main(argv=[''],verbosity=2,exit=False)

