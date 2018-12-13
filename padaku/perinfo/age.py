#!/usr/bin/env python
# coding: utf-8

# In[19]:


def age(time):
    from datetime import datetime
    t=datetime.strptime(str(time),"%Y-%m-%d")
    now = datetime.now()
    age=int((now-t).days/365)
    return 'The age of the person is {} years'.format(age)



