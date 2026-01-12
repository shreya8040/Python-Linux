import psutil

def get_cpu_perc():
		return psutil.cpu_percent(interval =1)
		


