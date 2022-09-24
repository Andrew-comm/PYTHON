import shutil
#cpu-usage
import psutil
#cpu-usage
def check_disk_usage():
    du=shutil.disk_usage(disk)
    
    free=(du.free/du.total)*100
      
    return free >20
def check_cpu_usage():
    psutil.cpu_percent(0.1)
    
if not check_disk_usage("/")or not check_cpu_usage():
    print("error")
    
else:

    print("everything is ok") 
    
    

