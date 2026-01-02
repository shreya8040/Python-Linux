import psutil
import plotext as plt
t=[];
r=10
s=[]
for x in range(r):
	plt.cld()
	plt.clt()
	s.append(' ')
	y=psutil.cpu_percent(interval=1)
	t.append(y)
	
	z=plt.bar(s,t)
	
	plt.show()
	

