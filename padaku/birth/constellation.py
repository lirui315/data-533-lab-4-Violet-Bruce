
# coding: utf-8

# In[13]:


def constellation(month,date):
    if (month==3 and date>=21) or (month==4 and date<=19):
        return "Your constellation is Aries"
    elif (month==4 and date>=20) or (month==5 and date<=20):
        return "Your constellation is Taurus"
    elif (month==5 and date>=21) or (month==6 and date<=21):
        return "Your constellation is Gemini"
    elif (month==6 and date>=22) or (month==7 and date<=22):
        return "Your constellation is Cancer"    
    elif (month==7 and date>=23) or (month==8 and date<=22):
        return "Your constellation is Leo"
    elif (month==8 and date>=23) or (month==9 and date<=22):
        return "Your constellation is Virgo"
    elif (month==9 and date>=23) or (month==10 and date<=23):
        return "Your constellation is Libra"
    elif (month==10 and date>=24) or (month==11 and date<=22):
        return "Your constellation is Scorpio" 
    elif (month==11 and date>=23) or (month==12 and date<=21):
        return "Your constellation is Sagittarius"
    elif (month==12 and date>=22) or (month==1 and date<=19):
        return "Your constellation is Capricornus"
    elif (month==1 and date>=20) or (month==2 and date<=18):
        return "Your constellation is Aquarius"
    else:
        return "Your constellation is Pisces"


# In[14]:




