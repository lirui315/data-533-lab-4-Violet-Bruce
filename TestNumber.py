
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
        self.assertMultiLineEqual(number.life_path_number(1994,4,19),"Your life path number is 1")
        self.assertMultiLineEqual(number.life_path_number(1975,11,29),"Your life path number is 8")
        self.assertMultiLineEqual(number.life_path_number(1974,7,29),"Your life path number is 3") 
        self.assertMultiLineEqual(number.life_path_number(0000,7,29),"Invalid Input") 
        self.assertMultiLineEqual(number.life_path_number(1994,'a',29),"Invalid Input")
        self.assertMultiLineEqual(number.life_path_number(1895,7,'c'),"Invalid Input")  
        self.assertMultiLineEqual(number.life_path_number('d',7,29),"Invalid Input")   
        self.assertMultiLineEqual(number.life_path_number(1974,7,2),"Your life path number is 3") 

    def tearDown(self):
        print('Tear Down')
    
    @classmethod    
    def tearDownClass(cls):
        print('teardownClass') 
unittest.main(argv=[''],verbosity=2,exit=False)

