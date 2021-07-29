import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pin): #7,11,13,15
        '''(self,list)

        '''
        # position of motor in degrees between -90 to 90
        self.pin = pin
        self.position = 0     
        
    def goto(self, position): #given position between -90 to 90
        #setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin,GPIO.OUT)
        
        self.position = position
        
        #unit conversion
        realPosition = position + 90
        ms = realPosition/180*2 + 0.4
        dc = int(100*(ms/20))
        
        #motor movement
        pwm = GPIO.PWM(self.pin,50)
        pwm.start(0)
        pwm.ChangeDutyCycle(dc)
        time.sleep(1)
        pwm.stop()
        GPIO.cleanup()
