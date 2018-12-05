#!/usr/bin/env python
# coding: utf-8

# In[60]:


def firstname(fullname):
    fullname=fullname.lower()
    Firstname=fullname.split()[0]
    Firstname=Firstname.capitalize()
    return ("Firstname:",Firstname)
def lastname(fullname):
    fullname=fullname.lower()
    Lastname=fullname.split()[1]
    Lastname=Lastname.capitalize()
    return ("Lastname:",Lastname)


# In[62]:


firstname("BRUCE PEI")


# In[61]:


lastname("BRUCE PEI")

