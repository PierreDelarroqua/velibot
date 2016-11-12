from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
import requests
from update import get_station_individual

NUMBER_STATION_BEGIN = "04006"
NUMBER_STATION_FINISH = "11011"

with open('config_velib.json', 'r') as f:
    config = json.load(f)

url = config["urls"]["root"] + config["urls"]["stations"]



@respond_to('velib', re.IGNORECASE)
def update_velib(message):  
        
    station_begin = get_station_individual(NUMBER_STATION_BEGIN)
    station_finish = get_station_individual(NUMBER_STATION_FINISH)
    
    result = "Station de départ : {0} \n Nombre de vélos disponibles : {1} \n\
    Station d'arrivée : {2} \n Nombre de places disponibles : {3} \n" \
    .format(station_begin["name"], station_begin["available_bikes"], station_finish["name"], station_finish["available_bike_stands"])
        
    message.reply(result)

#Todo : station_begin["available_bikes"] < 4 ou station_finish["available_bike_stands"] < 2, chercher la station la plus proche avec plus de disponibilités


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

