import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 
owm = OWM('bdf70656d92a66e8487a36cbb58ad9ab', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot( "1924042861:AAGNnSJmbLH-j8eWBjA5Lavu40toNtCHI-g", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text )
    observation = mgr.weather_at_place( message.text )
    w = observation.weather 
    temp = w.temperature('celsius')["temp"]
    
    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    
    answer += "Темперетару сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Холодно накинь куртку" 
    elif temp < 20:
        answer += "Тепло, можно в байке"
    else:
        answer += "Жарко иди в майке"
    
    bot.send_message(message.chat.id,answer )

bot.polling( none_stop = True )