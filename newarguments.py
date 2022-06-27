from datetime import datetime                                           ## Question 4
from datetime import timedelta

def main():                                                             ## main function to call the inches and feet function
    
    feet = input("feet: ")
    inches = input("inches: ")
    
    inchesandfeet(feet, inches)

    

def inchesandfeet(feet, inches):                                        ## inches and feet function

    dt = datetime.now()                                                 ## define dt at current date and time

    d = timedelta(days = 100, hours = 10, minutes = 13)                 ## create an object "d" that is adds 100 days, 10 hours, and 13 minutes ahead of current time

    ddt = dt + d                                                        ## add the datetime object and the timedelta object to project a future date that is 100 days, 10 hours, and 13 minutes ahead

    ft =int(feet)                                                       ## turn strings feet and inches into integers to be used by the if statement
    inch = int(inches)
    
    i = 0

    if ft <= 5 and inch <= 7:                                           ## if statement prints according to size of 2x4

        print("2x4 size delivery for:", feet + "ft", inches + "in on:", "\t", ddt)

        

    else:

        print("2x4 size deliverd for:", feet + "ft", inches + "in on:", "\t", dt)
        
    


main()                                                                  ## call main function