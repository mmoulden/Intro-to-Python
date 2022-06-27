from datetime import datetime               ##Question 2
from datetime import timedelta              

def main():
    dt = datetime.now()                     ## get current date and time

    red60sec = dt - timedelta(seconds = 60) ## reduce current time by 60 seconds

    inc2yr = dt + timedelta(days = 720)     ## add 720 days (2 years) to time (not accounting for leap years)

    print(red60sec, inc2yr)                 ##print both adjusted times

main()                                      ## call main function