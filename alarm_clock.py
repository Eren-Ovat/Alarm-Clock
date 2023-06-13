import time
from playsound import playsound

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # 125 // 60 = 2
        seconds_left = time_left % 60 # 125 % 60 = 5  

        print(f'{CLEAR_AND_RETURN}Timer :{minutes_left:02d}:{seconds_left:02d}')
    
    playsound('')  #Please write your file with the .mp3 extension here.
    
minutes = int(input('How many minutes should it be? : '))
seconds = int(input('How many seconds should it be? : '))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)







