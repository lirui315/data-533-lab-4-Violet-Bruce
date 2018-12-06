
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
        self.b1=birthdate.Birthinfo(1995,3,1)

        self.p1=birthdate.Year(1996,3,15)
        self.p2=birthdate.Year(1990,10,25)
        self.p3=birthdate.Year(1994,4,21)
        self.p4=birthdate.Year(1995,2,10)
        self.p5=birthdate.Year(1991,12,27)
        self.p6=birthdate.Year(1992,3,21)
        self.p7=birthdate.Year(1993,6,10)
        self.p8=birthdate.Year(1997,6,30)
        self.p9=birthdate.Year(1998,7,27)
        self.p10=birthdate.Year(1999,8,29)
        self.p11=birthdate.Year(2000,9,24)
        self.p12=birthdate.Year(2001,12,3)
        self.p13=birthdate.Year('aaaa','a',27)

        self.m1=birthdate.Month(1996,3,15)
        self.m2=birthdate.Month(1990,10,25)
        self.m3=birthdate.Month(1994,4,21)
        self.m4=birthdate.Month(1995,2,10)
        self.m5=birthdate.Month(1991,12,27)
        self.m6=birthdate.Month(1992,3,21)
        self.m7=birthdate.Month(1993,6,10)
        self.m8=birthdate.Month(1997,6,30)
        self.m9=birthdate.Month(1998,7,27)
        self.m10=birthdate.Month(1999,8,29)
        self.m11=birthdate.Month(2000,9,24)
        self.m12=birthdate.Month(2001,12,3)
        self.m13=birthdate.Month(2002,'a',27)
        print('Set Up')
    
    def test_birthdate(self):
        self.assertTupleEqual(self.b1.display(),('Year is 1995', 'Month is 3', 'Date is 1'))

        self.assertTupleEqual(self.p1.chinese_zodiac(),('Year is 1996', 'Chinese Zodiac is Rat'))
        self.assertTupleEqual(self.p2.chinese_zodiac(),('Year is 1990', 'Chinese Zodiac is Horse'))
        self.assertTupleEqual(self.p3.chinese_zodiac(),('Year is 1994', 'Chinese Zodiac is Dog'))
        self.assertTupleEqual(self.p4.chinese_zodiac(),('Year is 1995', 'Chinese Zodiac is Pig'))
        self.assertTupleEqual(self.p5.chinese_zodiac(),('Year is 1991', 'Chinese Zodiac is Goat')) 
        self.assertTupleEqual(self.p6.chinese_zodiac(),('Year is 1992', 'Chinese Zodiac is Monkey'))
        self.assertTupleEqual(self.p7.chinese_zodiac(),('Year is 1993', 'Chinese Zodiac is Rooster'))
        self.assertTupleEqual(self.p8.chinese_zodiac(),('Year is 1997', 'Chinese Zodiac is Ox'))
        self.assertTupleEqual(self.p9.chinese_zodiac(),('Year is 1998', 'Chinese Zodiac is Tiger'))
        self.assertTupleEqual(self.p10.chinese_zodiac(),('Year is 1999', 'Chinese Zodiac is Rabbit'))   
        self.assertTupleEqual(self.p11.chinese_zodiac(),('Year is 2000', 'Chinese Zodiac is Dragon'))
        self.assertTupleEqual(self.p12.chinese_zodiac(),('Year is 2001', 'Chinese Zodiac is Snake'))
        self.assertMultiLineEqual(self.p13.chinese_zodiac(),('Invalid Input'))
     
        self.assertMultiLineEqual(self.m1.constellation(),"Your constellation is Pisces")
        self.assertMultiLineEqual(self.m2.constellation(),"Your constellation is Scorpio")
        self.assertMultiLineEqual(self.m3.constellation(),"Your constellation is Taurus")
        self.assertMultiLineEqual(self.m4.constellation(),"Your constellation is Aquarius")
        self.assertMultiLineEqual(self.m5.constellation(),"Your constellation is Capricornus")  
        self.assertMultiLineEqual(self.m6.constellation(),"Your constellation is Aries")
        self.assertMultiLineEqual(self.m7.constellation(),"Your constellation is Gemini") 
        self.assertMultiLineEqual(self.m8.constellation(),"Your constellation is Cancer") 
        self.assertMultiLineEqual(self.m9.constellation(),"Your constellation is Leo")
        self.assertMultiLineEqual(self.m10.constellation(),"Your constellation is Virgo")
        self.assertMultiLineEqual(self.m11.constellation(),"Your constellation is Libra") 
        self.assertMultiLineEqual(self.m12.constellation(),"Your constellation is Sagittarius")    
        self.assertMultiLineEqual(self.m13.constellation(),"Invalid Input")     
    
    def tearDown(self):
        print('Tear Down')
        
    @classmethod    
    def tearDownClass(cls):
        print('teardownClass') 
        
unittest.main(argv=[''],verbosity=2,exit=False)

