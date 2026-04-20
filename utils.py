import psutil
import time

def get_bandwidth_usage():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    upload = net2.bytes_sent - net1.bytes_sent
    download = net2.bytes_recv - net1.bytes_recv

    return upload, download