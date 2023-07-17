import random
import time
m=100000
n1=[]
for i in range(m):
    n1 +=[random.randint(0,1000000)]
start_time = time.time()
def solexaustiva(m,n):
    res=0
    aux=0
    for i in range(m):
        for j in range(i+1,m):
            if(n[j]>=n[i]):
                aux=n[j]-n[i]   
            else:
                aux=n[i]-n[j] 
            if(aux>res):
                res=aux
    return res

result=solexaustiva(m,n1)
print("--- %s seconds ---" % (time.time() - start_time))


 
 


    
          
                
            
    
     
    
         
         
          
            
            
            
        
