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
		print(t)
		print("\033[A\033[A")
print("\n")
print(m)

def viz_t():
	return t


