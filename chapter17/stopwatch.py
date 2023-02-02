import time


import pyperclip


def stopwatch():
   
    
    print('enter to begin')
    input()                   
    print('started')
    clip = ''
    startTime = time.time()    #
    lastTime = startTime
    lapNum = 1

    
    
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        info = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).center(7), str(lapTime).rjust(6))
        clip += info + '\n'
        print(info, end='')
        lapNum += 1
        lastTime = time.time() 
    
        



stopwatch()
