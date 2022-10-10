import psutil
import time

def getCPU():
    return psutil.cpu_percent(interval=.01)

def getRAM():
    return psutil.virtual_memory()[2]

def getNET():
    interval = 1
    start_time = time.time()

    _download = psutil.net_io_counters().bytes_recv
    time.sleep(interval)

    end_time = time.time()
    _download1 = psutil.net_io_counters().bytes_recv
    download = (_download1 - _download) / (end_time - start_time)

    return round(download / 1000000, 3)

