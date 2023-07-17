import random
import time
m=125000
n1=[]
for i in range(m):
    n1 +=[random.randint(0,1000000)]
start_time = time.time()

def semordena(m,n):
    menor=n[0]
    maior=0
    for i in range(m):
        if(n[i]>maior):
            maior=n[i]
        elif(n[i]<menor):
            menor=n[i]
    return maior-menor

result=semordena(m,n1)
print("--- %s seconds ---" % (time.time() - start_time))

