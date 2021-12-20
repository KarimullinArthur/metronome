import time

bpm = int(input('BPM = '))
bpm = 60 / bpm
while True:
    print('\a',end='\rBeep')
    time.sleep(bpm)
