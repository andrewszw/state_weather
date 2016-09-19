#!usr/bin/python3

from bs4 import BeautifulSoup
import csv
import requests


def get_states():

    # list to store all state information in
    state_info = list()

    # store the url of the webpage to be scraped
    url = 'http://xfront.com/us_states/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # get all of the list elements
    li_list = soup.find_all('li')
    for li in li_list:
        p_list = li.find_all('p')

        # get the state name
        state_name = p_list[0].text
        state_name = state_name.split(':')[-1].strip()

        # get the state capital
        state_capital = p_list[1].text
        state_capital = state_capital.split(':')[-1].strip()

        # get the state longitude and latitude
        state_capital_long = p_list[2].text
        state_capital_long = state_capital_long.split(':')[-1].strip()
        state_capital_lat = p_list[3].text
        state_capital_lat = state_capital_lat.split(':')[-1].strip()

        # append all info gathered to list
        state_info.append([state_name, state_capital, state_capital_long, state_capital_lat])

    return state_info


def write_to_csv(state_info):

    # open the csv file to write to
    with open('state_capital_coords.csv', 'w', newline='') as csvfile:
        state_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for state in state_info:
            state_writer.writerow(state)


def main():
    
    # get the state capitals along with their latitudes/longitudes
    state_info = get_states()

    # write all state info to a csv file
    write_to_csv(state_info)

if __name__ == '__main__':
    main()
