import pyowm



city = input("Введите полное и корректное название города  (Киев,Москва,Берлин)")  
owm = pyowm.OWM('f4640c34aeefad5699689b2a83c23678')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("В городе " + city + " сейчас температура: " +str(temperature) + " по Цельсию.")
print("Также, в указаном городе " +w.get_detailed_status())



