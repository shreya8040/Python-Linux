from cpuperc import get_cpu_perc
import time
r=10
t=[]
for x in range(r):
		y=get_cpu_perc()
		t.append(y)
		
		print(t)
		print("\033[A\033[A")
print("\n")	


