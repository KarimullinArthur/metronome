import time

bpm = int(input())

bpm /= 60
while True:
    print('\a',end='\rBeep')
    time.sleep(bpm)
