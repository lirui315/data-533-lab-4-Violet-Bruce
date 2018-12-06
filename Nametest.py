#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from padaku.perinfo import nanur as n


# In[12]:


class TestName(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class")
    
    def setUp(self):
        print("Set Up")
    
    def test_age(self):    

        self.assertMultiLineEqual(n.name("@$%"),'invalid input') 
        self.assertMultiLineEqual(n.name(432),'Please input characters')
        self.assertTupleEqual(n.name("AI AI"),('Numerology magic for ai ai',
 'Initiator action, pioneering, leading, independent, attaining, and individualistic'))
        self.assertTupleEqual(n.name("Violet"),('Numerology magic for violet',
 'Cooperation, adaptability, consideration of others, partnering, and mediating')) 
        self.assertTupleEqual(n.name("JIM Mac"),('Numerology magic for jim mac',
 'Expression, verbalization, socialization, the arts, and the joy of living'))
        self.assertTupleEqual(n.name("DI"),('Numerology magic for di',
 'Values foundation, order, service, struggle against limits, and steady growth'))
        self.assertTupleEqual(n.name("Matt Rea"),('Numerology magic for matt rea',
 'Expansiveness, visionary, adventure, and the constructive use of freedom'))
        self.assertTupleEqual(n.name("Bruce Pei"),('Numerology magic for bruce pei',
 'Responsibility, protection, nurturing, community, balance, and sympathy'))
        self.assertTupleEqual(n.name("Sara King"),('Numerology magic for sara king',
 'Analysis, understanding, knowledge, awareness, studious, and meditating'))
        self.assertTupleEqual(n.name("Ba Bac"),(('Numerology magic for ba bac',
'Practical endeavors, status oriented, power-seeking, and high-material goals')))
        self.assertTupleEqual(n.name("Ba Baca"),(('Numerology magic for ba baca',
'Smart, intelligent, very helpful and warmhearted')))
        self.assertTupleEqual(n.name("CBBBB"),(('Numerology magic for cbbbb',
'Higher spiritual plane, intuitive, illumination, idealist, and a dreamer')))
        self.assertTupleEqual(n.name("Jiag Ma"),(('Numerology magic for jiag ma',
 'The Master Builder, large endeavors, powerful force, and leadership')))
        
    def tearDown(self):
        print("Tear Down")
    
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")
        
unittest.main(argv=[''],verbosity=2,exit=False)

