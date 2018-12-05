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
        
        self.assertTupleEqual(n.name("Bruce Pei"),('Numerology magic for Bruce Pei',
 'Responsibility, protection, nurturing, community, balance, and sympathy'))
        self.assertTupleEqual(n.name("Lijun Pei"),('Numerology magic for Lijun Pei',
 'Expansiveness, visionary, adventure, and the constructive use of freedom'))
        self.assertTupleEqual(n.name("Yang Lin"),('Numerology magic for Yang Lin',
 'The Master Builder, large endeavors, powerful force, and leadership'))
        self.assertTupleEqual(n.name("Kenny So"),('Numerology magic for Kenny So',
 'Expression, verbalization, socialization, the arts, and the joy of living'))
        self.assertTupleEqual(n.name("Grass Genius"),('Numerology magic for Grass Genius',
 'Expression, verbalization, socialization, the arts, and the joy of living'))
    
    def tearDown(self):
        print("Tear Down")
    
    @classmethod
    def tearDownClass(cls):
        print("teardownClass")
        
unittest.main(argv=[''],verbosity=2,exit=False)

