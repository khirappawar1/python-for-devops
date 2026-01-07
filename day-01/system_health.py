import psutil

#Get the threshold values 
cpu_threshold=int(input("Enter the threshold CPU %"))
disk_threshold=int(input("Enter the threshold Disk usage %"))
memory_threshold=int(input("Enter the threshold memory %"))

#Fetch the system metrics
current_cpu=psutil.cpu_percent(interval=1)
current_disk_usage=psutil.disk_usage('/').percent
current_memory_usage=psutil.virtual_memory().percent

#Print system metrics
print("cpu %",current_cpu)
print("Disk usage %:",current_disk_usage)
print("Memory usage %:",current_memory_usage)

if current_cpu>cpu_threshold:
    print("High CPU utilization")
else:
    print("CPU usage under threshold")
    if current_disk_usage>disk_threshold:
        print("Disk usage exceeded threshold")
    else:
        print("Disk usage under threshold")
        if current_memory_usage>memory_threshold:
            print("Memory usage exceeded threshold")
        else:
            print("Memory under threshold")
