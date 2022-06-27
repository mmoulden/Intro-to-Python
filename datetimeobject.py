from datetime import datetime                               ##Question 3
from datetime import timedelta

def main():
    dt = datetime.now()                                     ## set dt at current date and time

    d = timedelta(days = 100, hours = 10, minutes = 13)     ## create timedelta object that adds 100 days, 10 hours, and 13 minutes to current date and time

    ddt = dt + d                                            ## add timedelta to current time

    print(dt)                                               ##print both current date and time and the date and time + 100 days, 10 hours, and 30 minutes
    print(ddt)

main()                                                      ## call main function