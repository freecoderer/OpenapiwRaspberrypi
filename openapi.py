import pyowm import OWM

API_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
owm = OWM(API_key)

city = ['Seoul', 'Tokyo', 'London', 'New York', 'Paris', 'Sydney', 'Nairobi']

def get_weather(num):
    obs = owm.weather_at_place(city[num-1])
    w = obs.get_weather()
    location = obs.get_location().get_name() #지역
    ref_time = w.get_reference_time()
    detailed = w.get_detailed_status()
    temp = str(w.get_temperature(unit="celsius")['temp']) + "˚C" #온도
    humid = str(w.get_humidity()) + "%"  #습도
    temp_max = str(w.get_temperature(unit="celsius")['temp_max']) + "˚C" #최고온도
    temp_min = str(w.get_temperature(unit="celsius")['temp_min']) + "˚C" #최저온도
    windspeed = str(w.get_wind()['speed']) + "m/s" # 풍속
    sunrise = w.get_sunrise_time() # 일출
    sunset = w.get_sunset_time() # 일몰
    
    print("\nSelected Location :", location)
    print("Reference Time :", ref_time)
    print("Detailed Status :", detailed)
    print("Temperature_Now :", temp)
    print("Temperature_Max :", temp_max)
    print("Temperature_Min :", temp_min)
    print("Humidity :", humid)
    print("Sunrise Time :", sunrise)
    print("Sunset Time :", sunset)
    return

for i in range(7):
    print(i + 1, ":", city[i])
print("0 : Exit")

while 1:
    inum = int(input("\nChoose city number : "))

    if(inum == 0):
        print("Exit Program.")
        break
    elif(inum < 0 or inum > 7):
        print("Out of Range")
        continue
    get_weather(inum)
