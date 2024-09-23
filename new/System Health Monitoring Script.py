import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
        print(f"ALERT: High memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        logging.warning(f"Low disk space: {disk_usage.percent}% used")
        print(f"ALERT: Low disk space: {disk_usage.percent}% used")

def check_running_processes():
    # List all processes
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    for process in processes:
        if process['cpu_percent'] > CPU_THRESHOLD or process['memory_percent'] > MEMORY_THRESHOLD:
            logging.warning(f"Process {process['name']} (PID {process['pid']}) using too much resources: CPU {process['cpu_percent']}%, Memory {process['memory_percent']}%")
            print(f"ALERT: Process {process['name']} (PID {process['pid']}) is using too many resources: CPU {process['cpu_percent']}%, Memory {process['memory_percent']}%")

def monitor_system():
    logging.info("Starting system health check...")
    print("Starting system health check...")
    
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

    logging.info("System health check completed.")
    print("System health check completed.")

if __name__ == "__main__":
    monitor_system()
