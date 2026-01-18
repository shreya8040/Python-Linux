from cpuperc import get_cpu_perc
from memoryuse import get_mem_usage
import time
r = int(input("Enter time in seconds:"))
t=[]
m=get_mem_usage()
print("\n")
print(m)
for x in range(r):
		y=get_cpu_perc()
		t.append(y)





