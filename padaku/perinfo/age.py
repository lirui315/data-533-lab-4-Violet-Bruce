#!/usr/bin/env python
# coding: utf-8

# In[16]:


def age(time):
    from datetime import datetime
    t=datetime.strptime(str(time),"%Y-%m-%d")
    now = datetime.now()
    age=int((now-t).days/365)
    days=int((now-t).days%365)
    return 'The age of the person is {} and {} days'.format(age,days)


# In[17]:


age("1996-03-15")

