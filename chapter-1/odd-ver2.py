#import datetime function from datetime module
from datetime import datetime
#import time and random modules
import time
import random

#create an array with odd numbers up to 60
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

#adding for loop to repeat 5 times
for i in range(5):

    #set variable to current minute using datetime function
    right_this_minute = datetime.today().minute

    #if loop to print whether current minute is odd or not
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)

