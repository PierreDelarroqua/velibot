import json
import requests
from utils import *

import psycopg2
from datetime import datetime

with open('config_velib.json', 'r') as f:
    config = json.load(f)

url = config["urls"]["root"] + config["urls"]["stations"]

conn = None
conn = psycopg2.connect("dbname='velib' user='pierredelarroqua' host='localhost'")
cur = conn.cursor()



def scrape_stations():
    stations_list = get_stations_list()
    
    for result in stations_list:
    	result["last_update_clean"] = convert_timestamp(result["last_update"])
    	query = "INSERT INTO data_from_api.all_stations_updates (datetime, response_api) VALUES (%s, %s)"
    	cur.execute(query,(datetime.now(), json.dumps(result)))
    	conn.commit()

def get_stations_list():
    response = requests.get(url, params = config["params"])
    return json.loads(response.content.decode("utf8"))

def get_station_individual(number_station):
	url_station = url + "/" + number_station
	response = requests.get(url_station, params = config["params"])
	return json.loads(response.content.decode("utf8"))
