
def age(time):
    try:
        try:
            from datetime import datetime
            t=datetime.strptime(str(time),"%Y-%m-%d")
        #t=time.split("-")
        except:
            return "datetime error"
        #print(t,type(t))
        
    
        now = datetime.now()
    
        age=int((now-t).days/365)
            
        return 'The age of the person is {} years'.format(age)
        
    except:
            return "error in input"