#! python3
import time

print('Press enter to stop or resume the stopwatch.')

lapNum = 1
startTime = time.time()
lastTime = startTime

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(6), str(lapTime).rjust(6)), end='')
        lapNum += 1    
        lastTime = time.time()        
except KeyboardInterrupt:
    print('Done!')