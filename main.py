
#camdown program in python

import time 

my_time  = int(input("Enter the time in seconds:"))

#Taken simple time seconds

#for X in range(0 ,my_time):                                  # 1 program
#    print(X)
#    time.sleep(1)

#print("TIME'S UP")


#Taken some oter or upgrated functions----->                    #  2 program

for X in range(my_time, 0, -1):
    seconds = X % 60
    minutes = int(X / 60) % 60
    hours = int(X /3600)    #3600 seconds in 1 hour

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")