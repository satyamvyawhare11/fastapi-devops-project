import psutil

def fetch_system_stats():
    cpu_load = psutil.cpu_percent(interval=1)
    ram_load = psutil.virtual_memory().percent
    disk_load = psutil.disk_usage("/").percent

    data = {
        "cpu": cpu_load,
        "ram": ram_load,
        "disk": disk_load
    }

    return data
