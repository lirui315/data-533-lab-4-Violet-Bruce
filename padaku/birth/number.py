
# coding: utf-8

# In[ ]:


def life_path_number(year,month,date):
    yearnum=0
    monthnum=0
    datenum=0
    for i in range(0,4):
        yearnum+=int(str(year)[i])
    if yearnum>=10 and yearnum!=11 and yearnum!=22:
        yearnum=int(str(yearnum)[0])+int(str(yearnum)[1])
    if month>=10:
        for i in range(0,2):
            monthnum+=int(str(month)[i])
    else:
        monthnum=month
    if date>=10:
        for i in range(0,2):
            datenum+=int(str(date)[i])
    else:
        datenum=date
    if datenum>=10 and datenum!=11 and datenum!=22:
        datenum=int(str(datenum)[0])+int(str(datenum)[1])
    lpn=yearnum+monthnum+datenum
    if lpn>=10 and lpn!=11 and lpn!=22:
        lpn=int(str(lpn)[0])+int(str(lpn)[1])
    return "Your life path number is "+str(lpn)

