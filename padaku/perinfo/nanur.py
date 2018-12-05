#!/usr/bin/env python
# coding: utf-8

# In[41]:


def name(name):
    name1=str(name).lower()
    num =[]
    sum=0
    pred=['Initiator action, pioneering, leading, independent, attaining, and individualistic',          'Cooperation, adaptability, consideration of others, partnering, and mediating',          'Expression, verbalization, socialization, the arts, and the joy of living',          'Values foundation, order, service, struggle against limits, and steady growth',          'Expansiveness, visionary, adventure, and the constructive use of freedom',          'Responsibility, protection, nurturing, community, balance, and sympathy',          'Analysis, understanding, knowledge, awareness, studious, and meditating',          'Practical endeavors, status oriented, power-seeking, and high-material goals',          'Humanitarian, giving nature, selflessness, obligations, and creative expression',          'Higher spiritual plane, intuitive, illumination, idealist, and a dreamer',          'The Master Builder, large endeavors, powerful force, and leadership']
    for i in name1:
        num.append((int(ord(i))-96)%9)
    for j in num:
        sum+=j
    if sum!=11 and sum!= 22:
        sum=sum%9
    for k in range(0,10):
        if sum==k:
            return "Numerology magic for {}".format(name), pred[k-1]
    if sum==11:
        return "Numerology magic for {}".format(name), pred[9]
    if sum==22:
        return "Numerology magic for {}".format(name), pred[10]

