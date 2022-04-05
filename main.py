# Модуль pip install pyown
# API https://home.openweathermap.org/

import pyowm

owm = pyowm.OWM('3f711a4c7d088a182fa4fb77e8b6f88e')
mgr = owm.weather_manager()


user_name = input('Введите имя: ')
place = input('Какой город/страна? (пример New-York/Moscow/London): ')

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print(user_name + ', в городе ' + place + ' сейчас ' + w.detailed_status)
print('Температура сейчас ' + str(temp))

if temp < 10:
    print('Холодно, оденься потеплее чувак')
elif temp < 20:
    print('Сейчас прохладно, не забудь накинуть что-нибудь')
else:
    print('Тепло!')