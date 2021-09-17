from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ru' 
owm = OWM('bdf70656d92a66e8487a36cbb58ad9ab', config_dict)
mgr = owm.weather_manager()


place = input ('В каком городе/стране?: ')

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print( "В городе " + place + " сейчас " + w.detailed_status )
print ( "Темперетару сейчас в районе " + str(temp))

if temp < 10:
    print ( "Холодно накинь куртку" )
elif temp < 20:
    print ( "Тепло, можно в байке" )
else:
    print ( "Жарко иди в майке" )