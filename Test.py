import pyowm 

city = input("Город блять")  
owm = pyown.OWM('API')<<<<<<<#Я в душе не эбу де взять API ключ  погоди Києва.
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperatue('celsius')['temp']

print(" В городе  " +city +"температура:" +str(temperature)+"по Цельсию.")
print(" В указаном городе" +w.get_detailed_status())
