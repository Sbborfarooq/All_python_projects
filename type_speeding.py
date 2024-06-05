from time import *
import random as r

#making function 
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        #range funtion should run according to paratest 
        try:
            if paratest[i] != usertest[i]:

                error=error+1
        except:
            error=error+1
    return error

#creating function for time delay 
def speed_time(time_s,time_e,userinput):
    time_delay=time_e -time_s
    time_r=round(time_delay,2)
    speed=len(userinput)/time_r
    return round(speed)



#now we will create the variable test 
test=["she sell sea shells on the sea shore","my name is sabbor farooq","iam python developer"]
test1=r.choice(test)
print("***** typing speed *****")
print(test1)
#till here our random module is properly working 

time1=time()
testinput=input("Enter :")
time2=time()

print('speed : ',speed_time(time1,time2,testinput),"w/sec")
print("Error :" ,mistake(test1,testinput)                     )