from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
API = ('1d6a967c57b93112aadd98bf7f58e480')
owm = OWM(API, config_dict)
mgr = owm.weather_manager()

place = input("Gorod vvedi: ")
observation = mgr.weather_at_place('place')
w = observation.weather

temp = w.temperature('celsius') ['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(temp)