import psutil
def get_mem_usage():
	print(psutil.virtual_memory())

export default get_mem_usage();
