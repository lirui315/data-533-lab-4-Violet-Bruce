
# coding: utf-8

# In[23]:


class Birthinfo:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date
    def display(self):
        return 'Year is %s'%self.year,'Month is %s'%self.month,'Date is %s'%self.date


# In[38]:





# In[36]:


class Year(Birthinfo):
    def __init__(self,year,month,date):
        Birthinfo.__init__(self,year,month,date)
    def chinese_zodiac(self):
        if self.year%12==4:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rat'
        elif self.year%12==5:
            return 'Year is %s'%self.year,'Chinese Zodiac is Ox'
        elif self.year%12==6:
            return 'Year is %s'%self.year,'Chinese Zodiac is Tiger'
        elif self.year%12==7:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rabbit'
        elif self.year%12==8:
            return 'Year is %s'%self.year,'Chinese Zodiac is Dragon'
        elif self.year%12==9:
            return 'Year is %s'%self.year,'Chinese Zodiac is Snake'
        elif self.year%12==10:
            return 'Year is %s'%self.year,'Chinese Zodiac is Horse'
        elif self.year%12==11:
            return 'Year is %s'%self.year,'Chinese Zodiac is Goat'
        elif self.year%12==0:
            return 'Year is %s'%self.year,'Chinese Zodiac is Monkey'
        elif self.year%12==1:
            return 'Year is %s'%self.year,'Chinese Zodiac is Rooster'
        elif self.year%12==2:
            return 'Year is %s'%self.year,'Chinese Zodiac is Dog'
        elif self.year%12==3:
            return 'Year is %s'%self.year,'Chinese Zodiac is Pig'


# In[37]:
class Month(Birthinfo):
    def __init__(self,year,month,date):
        Birthinfo.__init__(self,year,month,date)
    def constellation(self):
        if (self.month==3 and self.date>=21) or (self.month==4 and self.date<=19):
            return "Your constellation is Aries"
        elif (self.month==4 and self.date>=20) or (self.month==5 and self.date<=20):
            return "Your constellation is Taurus"
        elif (self.month==5 and self.date>=21) or (self.month==6 and self.date<=21):
            return "Your constellation is Gemini"
        elif (self.month==6 and self.date>=22) or (self.month==7 and self.date<=22):
            return "Your constellation is Cancer"    
        elif (self.month==7 and self.date>=23) or (self.month==8 and self.date<=22):
            return "Your constellation is Leo"
        elif (self.month==8 and self.date>=23) or (self.month==9 and self.date<=22):
            return "Your constellation is Virgo"
        elif (self.month==9 and self.date>=23) or (self.month==10 and self.date<=23):
            return "Your constellation is Libra"
        elif (self.month==10 and self.date>=24) or (self.month==11 and self.date<=22):
            return "Your constellation is Scorpio" 
        elif (self.month==11 and self.date>=23) or (self.month==12 and self.date<=21):
            return "Your constellation is Sagittarius"
        elif (self.month==12 and self.date>=22) or (self.month==1 and self.date<=19):
            return "Your constellation is Capricornus"
        elif (self.month==1 and self.date>=20) or (self.month==2 and self.date<=18):
            return "Your constellation is Aquarius"
        else:
            return "Your constellation is Pisces"


