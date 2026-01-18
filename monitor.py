from cpuperc import get_cpu_perc
from memoryuse import get_mem_usage
import plotext as plt
import time

t=[]
m=get_mem_usage()
print("Select the statistic to be displayed:\n1.CPU Usage for a window of time\n2.Memory Usage\n")
choice =int(input("Choice: "))
if choice==1:
	r=int(input("\nEnter the time for window in seconds: "))
	print("\nLoading...")
	for x in range(r):
		y=get_cpu_perc()
		t.append(y)
		
	liveuse =[]
	plt.canvas_color('black')
	plt.ylim(0,100)
	plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
	max_points = 10
	scroll_index=0
	plt.plotsize(300,700)
	for z in t:
		liveuse.append(z)
		scroll_index+=1
		start=max(0,scroll_index-max_points)
		end = scroll_index
		if len(liveuse)>max_points:
			liveuse.pop(0)
		v=list(range(start,end))
		s=[100]*len(t)
		plt.clt()
		plt.cld()
		plt.bar(v,liveuse, color = 'cyan')
		plt.plot(v,s,color= 'black')
		plt.show()
		time.sleep(1)

elif choice==2:
	print("\n")
	print(m)
	print("\n")

else:
	print("Invalid choice")


