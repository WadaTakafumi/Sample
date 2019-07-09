from numpy.random import * 
import time
start_time = time.perf_counter() 

a=rand(20,86400)
r1=randint(20)
r2=randint(20)

a[r1]=a[r1]*10
a[r2]=a[r2]**2
print(a)

print("perf_counter = {:.7f}".format(time.perf_counter() - start_time))