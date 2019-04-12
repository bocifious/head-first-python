from datetime import datetime # imports datetime function

#creating an array of odd numbers for 1-60 (seconds)
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

#set variable right_this_minute to equal datetime today function
#to the minute.  Will pull minute of current time
right_this_minute = datetime.today().minute

#if function to print statement if the time is found in the array
#else statement if time is not found in array
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")