from datetime import datetime               ##Question 1

def main():
    dt = datetime.now()                     ## get current date and time
    
    time = dt.strftime("%X")                ## create time, get only the current time
    
    print(time)                             ## print time

main()                                      ## call main function
