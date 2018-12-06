
# coding: utf-8

# In[2]:


import unittest
from padaku.birth import birthdate


# In[4]:


class TestBirthdateMonth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    def setUp(self):
        self.p1=birthdate.Month(1996,3,15)
        self.p2=birthdate.Month(1990,10,25)
        self.p3=birthdate.Month(1994,4,21)
        self.p4=birthdate.Month(1995,11,6)
        self.p5=birthdate.Month(1991,12,27)
        print('Set Up')
        
    def test_birthdate(self):
        self.assertMultiLineEqual(self.p1.constellation(),"Your constellation is Pisces")
        self.assertMultiLineEqual(self.p2.constellation(),"Your constellation is Scorpio")
        self.assertMultiLineEqual(self.p3.constellation(),"Your constellation is Taurus")
        self.assertMultiLineEqual(self.p4.constellation(),"Your constellation is Scorpio")
        self.assertMultiLineEqual(self.p5.constellation(),"Your constellation is Capricornus")  
        
    def tearDown(self):
        print('Tear Down')
        
    @classmethod    
    def tearDownClass(cls):
        print('teardownClass')  
        
unittest.main(argv=[''],verbosity=2,exit=False)

