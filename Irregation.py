import RPi.GPIO as GPIO 
import time
from time import sleep
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


water rate = 21 # soil sensor
relay = 4

GPIO.setup(relay, GPIO.OUT)
GPIO.setup(channel, GPIO.IN)




print("Starting....") 
     
def getSensorData(channel):
         
         print(f"water rate =  {water rate}") 
            
         if GPIO.input(water rate) >= 7:
               GPIO.output(relay, GPIO.LOW)
               print("pump is oN")

               #turn GPIO pin 21 on
         elif GPIO.input(water rate) < 7:
               GPIO.output(relay, GPIO.HIGH) #Turn GPIO pin 21 off
               print("pump is oFF")
   


def main():
    
    print ('Starting...')
        
    while True:        #Condition for repetitive running of the loop
                try:       
                    getSensorData(water rate)
                    payload = requests.post(" Enter your thingspeak link here  to display the water rate as graph " + str(water rate))


                except:           #Exception Block for handling exceptions 

                    print ('Exiting.')
                    break

# calling main function

if __name__ == '__main__':

    main()   



