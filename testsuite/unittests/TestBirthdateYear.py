
# coding: utf-8

# In[3]:


import unittest
from padaku.birth import birthdate


# In[4]:


class TestBirthdateYear(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    def setUp(self):
        self.p1=birthdate.Year(1996,3,15)
        self.p2=birthdate.Year(1990,10,25)
        self.p3=birthdate.Year(1994,4,21)
        self.p4=birthdate.Year(1995,11,6)
        self.p5=birthdate.Year(1991,12,27)
        print('Set Up')
    
    def test_birthdate(self):
        self.assertTupleEqual(self.p1.chinese_zodiac(),('Year is 1996', 'Chinese Zodiac is Rat'))
        self.assertTupleEqual(self.p2.chinese_zodiac(),('Year is 1990', 'Chinese Zodiac is Horse'))
        self.assertTupleEqual(self.p3.chinese_zodiac(),('Year is 1994', 'Chinese Zodiac is Dog'))
        self.assertTupleEqual(self.p4.chinese_zodiac(),('Year is 1995', 'Chinese Zodiac is Pig'))
        self.assertTupleEqual(self.p5.chinese_zodiac(),('Year is 1991', 'Chinese Zodiac is Goat'))       
    
    def tearDown(self):
        print('Tear Down')
        
    @classmethod    
    def tearDownClass(cls):
        print('teardownClass') 
        
unittest.main(argv=[''],verbosity=2,exit=False)

