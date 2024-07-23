import RPi.GPIO as GPIO
import time
from pyowm import OWM

GPIO.setmode(GPIO.BOARD)
led1 = 11
led2 = 13
led3 = 15
pin1 = 12 
pin2 = 16
fan = 3

GPIO.setup(led1,  GPIO.OUT)
GPIO.setup(led2,  GPIO.OUT)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.setwarnings(False)
p=GPIO.PWM(fan,100) 
p1 = GPIO.PWM(pin1, 50) 
p2 = GPIO.PWM(pin2, 50) 
p1.start(0)
p2.start(0)
cnt = 0

API_key = '838ab952a838802f1eb19938a2b447ff'
owm = OWM(API_key)

city = ['Seoul', 'Tokyo', 'London', 'New York', 'Paris', 'Sydney', 'Nairobi']

def setGPIO(temp2, humid2, windex)
    if(temp2 <= 20):
        GPIO.output(led1, True)
        p.stop()
    else:
        GPIO.output(led1, False)
        p.start(100)
        
    if(humid2 >= 40):
        GPIO.output(led2, True)
    else:
        GPIO.output(led2, False)
        
    if(windex[0] == '7' or windex[0] == '8'):
        p1.ChangeDutyCycle(1)
        p2.ChangeDutyCycle(1)
        time.sleep(1)
    else:
        p1.ChangeDutyCycle(8)
        p2.ChangeDutyCycle(8)
        time.sleep(1)

def get_weather(num):
    obs = owm.weather_at_place(city[num-1])
    w = obs.get_weather()
    location = obs.get_location().get_name()
    ref_time = w.get_reference_time()
    detailed = w.get_detailed_status()
    temp = str(w.get_temperature(unit="celsius")['temp']) + "˚C"
    temp2 = float(w.get_temperature(unit="celsius")['temp'])
    humid = str(w.get_humidity()) + "%"
    humid2 = float(w.get_humidity())
    temp_max = str(w.get_temperature(unit="celsius")['temp_max']) + "˚C"
    temp_min = str(w.get_temperature(unit="celsius")['temp_min']) + "˚C"
    windspeed = str(w.get_wind()['speed']) + "m/s"
    sunrise = w.get_sunrise_time()
    sunset = w.get_sunset_time()
    windex = str(w.get_weather_code())
    
    print("\nSelected Location :", location)
    print("Reference Time :", ref_time)
    print("Detailed Status :", detailed)
    print("Temperature_Now :", temp)
    print("Temperature_Max :", temp_max)
    print("Temperature_Min :", temp_min)
    print("Humidity :", humid)
    print("Sunrise Time :", sunrise)
    print("Sunset Time :", sunset)
    print("Weather Code:", windex)

    setGPIO(temp2, humid2, windex)

for i in range(7):
    print(i + 1, ":", city[i])
print("0 : Exit")

while 1:
    inum = int(float(input("\nChoose city number : ")))

    if(inum == 0):
        print("Exit Program.")
        GPIO.output(led1, False)
        GPIO.output(led2, False)
        p1.stop()
        p2.stop()
        GPIO.cleanup()
        break
    elif(inum < 0 or inum > 7):
        print("Out of Range")
    else:
        get_weather(inum)
