import time
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,2);

for i in range(5):
    time.sleep(second);
    print(123)