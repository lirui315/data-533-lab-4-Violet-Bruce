#!/usr/bin/env python
# coding: utf-8

# In[2]:


import testsuite.unittests.Agetest


# In[4]:


import unittest
import testsuite.unittests.TestBirthdateMonth as m
import testsuite.unittests.TestBirthdateYear as y
import testsuite.unittests.Agetest as a
import testsuite.unittests.Nametest as n



def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(m.TestBirthdateMonth))
    suite.addTest(unittest.makeSuite(y.TestBirthdateYear))
    suite.addTest(unittest.makeSuite(a.TestAge))
    suite.addTest(unittest.makeSuite(n.TestName))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()


# In[ ]:




