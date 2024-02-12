# libraries for MOSFET and servo control through GPIO pis
import RPi.GPIO as GPIO
from time import sleep
import keyboard 
GPIO.cleanup()
import keyboard
from server import Server
import socket

# instantiate TCP server
TCPserver = Server(12345)


# Setup the GPIO pins for MOSFET
GPIO.setmode(GPIO.BCM)

# maxes and mins for servo motion
PAN_MAX = 13
PAN_MIN = 2.6

TILT_MAX = 12
TILT_MIN = 2.5

TRIGGER_MAX = 9
TRIGGER_MIN = 1.8

# standard increment value for moving servos
SERVO_INCREMENT = 0.1

# set pins for servos
panServo = 17
GPIO.setup(panServo, GPIO.OUT)
panServo = GPIO.PWM(panServo, 50)
panServo.start(PAN_MIN)

tiltServo = 27
GPIO.setup(tiltServo, GPIO.OUT)
tiltServo = GPIO.PWM(tiltServo, 50)
tiltServo.start(TILT_MIN)

triggerServo = 18
GPIO.setup(triggerServo, GPIO.OUT)
triggerServo = GPIO.PWM(triggerServo, 50)
triggerServo.start(TRIGGER_MIN)

# setup MOSFET
mosfetPin = 4
GPIO.setup(mosfetPin, GPIO.OUT)


#other servo variables
panServoDuty = PAN_MIN
panServo.ChangeDutyCycle(panServoDuty)

tiltServoDuty = TILT_MIN
tiltServo.ChangeDutyCycle(tiltServoDuty)

triggerServoDuty = TRIGGER_MIN
triggerServo.ChangeDutyCycle(triggerServoDuty)



# function to control servo motors
def changeServoDuty(duty, decrease, increment, min, max):
  if (decrease and duty - increment >= min):
    return duty - increment
  elif (not decrease and duty + increment <= max):
    return duty + increment
  # return with no change if out of bounds
  return duty



# ---------------------------------------------------------------------
# main loop
# ---------------------------------------------------------------------

# initialize serverData before the loop starts
# check byte data interpretation file in docs
clientData = b'00000000'

while True:

  # check if there is data to retreive
  # this lets us avoid blocking with the data retrieval
  isData = TCPserver.getData(peek=True)
  if isData:
    # actually retrieve the server data
    clientData = TCPserver.getData()

  # ends the program from the client-side
  if clientData ==b'stop':
    break

  # variables to interpret the server input
  dcMotorState = clientData[0]
  dirSel0 = clientData[1]
  dirSel1 = clientData[2]
  moving = clientData[3]
  # tbd = clientData[4]
  speed = clientData[5]
  trigger = clientData[6]
  automatic = clientData[7]


  # moving directional servos based on dirSel
  # see dirSel table in docs
  if moving:
    if dirSel0:
      panServoDuty = changeServoDuty(panServoDuty, dirSel1, SERVO_INCREMENT, PAN_MIN, PAN_MAX)
      panServo.ChangeDutyCycle(panServoDuty)
      sleep(0.05)
    else:
      tiltServoDuty = changeServoDuty(tiltServoDuty, dirSel1, SERVO_INCREMENT, TILT_MIN, TILT_MAX)
      tiltServo.ChangeDutyCycle(tiltServoDuty)
      sleep(0.05)


  # turn on MOSFET for DC motor if it's supposed to be on
  if dcMotorState:
    GPIO.output(mosfetPin, 1)

    # trigger can only be pulled if the motor is running
    if trigger:
      triggerServoDuty = TRIGGER_MAX
      triggerServo.ChangeDutyCycle(triggerServoDuty)
      sleep(0.1)
      triggerServoDuty = TRIGGER_MIN
      triggerServo.ChangeDutyCycle(triggerServoDuty)
      
  # make sure MOSFET is off otherwise
  else:
    GPIO.output(mosfetPin, 0)


  if keyboard.is_pressed("c"):
    print("closing")
    break


TCPserver.closeServer()
GPIO.cleanup()
