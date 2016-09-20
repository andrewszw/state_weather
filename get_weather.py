import requests
import time
from datetime import datetime
import json
import csv


def display_weather(capital):
    url = 'https://api.darksky.net/forecast/813e95bf2800ea9b4abce322a87afad4/' + capital[2] + ',' + capital[3]
    f = requests.get(url)
    json_string = f.text
    parsed_json = json.loads(json_string)
    
    print("%s, %s: %s degrees F" % (capital[0], capital[1], parsed_json['currently']['temperature'])) 


def get_state_list():

    state_list = list()

    with open('state_capital_coords.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            state_list.append(row)

    return state_list


def main():
    state_list = get_state_list()
    for capital in state_list:
        display_weather(capital)


if __name__ == '__main__':
    main()
