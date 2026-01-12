import psutil
import plotext as plt
import numpy as np
t=[];
r=5
s=[100,100,100,100,100]
for x in range(r):
	
	y=psutil.cpu_percent(interval =0.8)
	t.append(y)
	
z=plt.bar(t,s)
plt.show()
