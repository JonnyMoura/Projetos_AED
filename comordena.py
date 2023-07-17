import time
import random
m=125000
n1=[]
for i in range(m):
    n1 +=[random.randint(0,1000000)]
start_time = time.time()
n1.sort()
def ordena(m,n):
    res=n[m-1]-n[0]
    return res
result=ordena(m,n1)
print("--- %s seconds ---" % (time.time() - start_time))


