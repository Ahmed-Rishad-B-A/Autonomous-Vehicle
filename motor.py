import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)			
GPIO.setmode(GPIO.BOARD)



GPIO.setup(12,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
pr_pwm = GPIO.PWM(12,1000)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
pl_pwm = GPIO.PWM(32,1000)

GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
prb_pwm = GPIO.PWM(35,1000)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
plb_pwm = GPIO.PWM(33,1000)
def control(dir,val):
    
    		#create PWM instance with frequency
    pr_pwm.start(0)				#start PWM of required Duty Cycle 
    pr_pwm.ChangeDutyCycle(val)  
    
    if(dir == "L" or dir == "l"):
        GPIO.output(40,1)
        GPIO.output(38,0)
        
    if(dir == "R" or dir == "r"):
        GPIO.output(40,0)
        GPIO.output(38,1)
        
    pl_pwm.start(0)				#start PWM of required Duty Cycle 
    pl_pwm.ChangeDutyCycle(val)  
    
    if(dir == "L" or dir == "l"):
        GPIO.output(36,1)
        GPIO.output(37,0)
        
    if(dir == "R" or dir == "r"):
        GPIO.output(36,0)
        GPIO.output(37,1)


def btyre():
    prb_pwm.start(0)				#start PWM of required Duty Cycle 
    prb_pwm.ChangeDutyCycle(50)
    
    plb_pwm.start(0)				#start PWM of required Duty Cycle 
    plb_pwm.ChangeDutyCycle(50)
    
    GPIO.output(29,1)
    GPIO.output(31,0)
    
    GPIO.output(32,1)
    GPIO.output(36,0)
    
control('l',100)
#lcontrol('l',100)