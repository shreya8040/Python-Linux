import psutil
import plotext as plt
t=[];
r=5
for x in range(r):
	y=psutil.cpu_percent(interval=1)
	t.append(y)
	print(t)
	if(x==(r-1)):
		exit()
	print("\033[A\033[A")
	
print(t)
		
	
	


