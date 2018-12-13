#!/usr/bin/env python
# coding: utf-8

# In[2]:




# In[4]:


import unittest
import TestBirthdate as b
import TestNumber as N
import Agetest as a
import Nametest as n


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(b.TestBirthdate))
    suite.addTest(unittest.makeSuite(N.TestNumber))
    suite.addTest(unittest.makeSuite(a.TestAge))
    suite.addTest(unittest.makeSuite(n.TestName))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[ ]:




