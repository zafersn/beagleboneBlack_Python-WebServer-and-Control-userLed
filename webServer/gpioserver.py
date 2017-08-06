from bottle import route, run, template, request
import Adafruit_BBIO.GPIO as GPIO
import beaglebone_userled.pythonled as pythonled


#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup("P8_10", GPIO.OUT)
user0 = pythonled(0)

current_values = {"user0": "off"}
#user0.off()
#user0.on()

@route('/')
def index():
    return template('gpio_template', current_values=current_values)


@route('/toggle', method='POST')
def toggle():
    pin = (request.query.pin)
    print pin
    print current_values[pin]
  #  current_values[pin] = not current_values[pin]
 #   GPIO.output(pin, current_values[pin])
    if current_values[pin]=="off":
	user0.off()
	current_values[pin]="on"
    else :
	user0.on()
	current_values[pin]="off"
    return template('gpio_template', current_values=current_values)

try:
    run(host='0.0.0.0', port=8081)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
