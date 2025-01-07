from packages import State
state = State()
from time import sleep

from gpiozero import LED, PWMLED

led1 = PWMLED(17)

ssh = PWMLED(24)

while state.reader(0):
    sleep(0.125) # -> 1/8

    
    led1.value = 0.2



    sleep(0.125) # -> 2/8





    sleep(0.125) # -> 3/8
    
    led1.value = 0


    sleep(0.125) # -> 4/8



    sleep(0.125) # -> 5/8
    
    if state.reader(1): ssh.value = 0.2
    else: ssh.off()    
    
    sleep(0.125) # -> 6/8
    
    ssh.value = 0   
    
    sleep(0.125) # -> 7/8

    if state.reader(1): ssh.value = 0.2
    else: ssh.value = 0    
    
    sleep(0.125) # -> 8/8

    ssh.value = 0