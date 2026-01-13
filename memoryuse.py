import psutil
def get_mem_usage():
	return psutil.virtual_memory()

