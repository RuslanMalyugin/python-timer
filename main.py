import time
from datetime import datetime

def print_time_every_10_seconds():
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)

print_time_every_10_seconds()
