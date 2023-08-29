import time
minutter = 0
sekunder = 0
tideler = 0

try:
    while True:
        for sekunder in range(60):
            for tideler in range(10):
                time.sleep(0.1)
                tideler += 1
            sekunder += 1
        minutter += 1
except KeyboardInterrupt:
    print('Tiden var: ',minutter,":",sekunder,".",tideler,sep="")