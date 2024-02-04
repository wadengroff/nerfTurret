# libraries for MOSFET and servo control through GPIO pis
import RPi.GPIO as GPIO
from time import sleep
import keyboard 
GPIO.cleanup()
import keyboard

# Setup the GPIO pins for MOSFET
GPIO.setmode(GPIO.BCM)

# set pins for servos
panServo = 17
GPIO.setup(panServo, GPIO.OUT)
panServo = GPIO.PWN(panServo, 50)

tiltServo = 27
GPIO.setup(tiltServo, GPIO.OUT)
tiltServo = GPIO.PWM(tiltServo, 50)
tiltServo.start(2.5)

triggerServo = 18
GPIO.setup(triggerServo, GPIO.OUT)
triggerServo = GPIO.PWM(triggerServo, 50)
triggerServo.start(1.8)

# setup MOSFET
mosfetPin = 4
GPIO.setup(mosfetPin, GPIO.OUT)


#other servo variables
panServoDuty = 13
panServ.ChangeDutyCycle(panServoDuty)

titleServoDuty = 2.5
tileServo.ChangeDutyCycle(tiltServoDuty)

triggerServoDuty = 1.8
triggerServo.ChangeDutyCycle(triggerServoDuty)


while True:
  # move the pan servo based on keyboard input
  if keyboard.is_pressed("right"):
    panServoDuty -= 0.1 if panServoDuty >=2.6 else 0
    panServo.ChangeDutyCycle(panServoDuty)
    sleep(0.05)
  elif keyboard.is_pressed("left"):
    panServoDuty += 0.1 if panServoDuty <= 13 else 0
    panServo.ChangeDutyCycle(panServoDuty)
    sleep(0.05)

  # move the tile servo based on keyboard input
if keyboard.is_pressed("up"):
  tiltServoDuty -= 0.1 if tiltServoDuty >= 2.6 else 0
  sleep(0.05)
elif keyboard.is_pressed("down"):
  tiltServoDuty += 0.1 if tiltServoDuty <= 12 else 0
  tiltServo.ChangeDutyCycle(tiltServoDuty)
  sleep(0.05)

# turn on MOSFET when space key is pressed
if keyboard.is_pressed("space"):
  GPIO.output(mosfetPin, 1)
  #can only pull the trigger while the motor is going
  if keyboard.is_pressed("s"):
    triggerServoDuty = 9
    triggerServo.ChangeDutyCycle(triggerServoDuty)
    sleep(0.5)
    triggerServoDuty = 1.7
    triggerServo.ChangeDutyCycle(triggerServoDuty)
  else:
    GPIO.output(mosfetPin, 0)
  if keyboard.is_pressed("c"):
    break


GPIO.cleanup()
