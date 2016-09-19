from bs4 import BeautifulSoup
import csv
import requests


def main():
    # store the url of the webpage to be scraped
    url = 'http://xfront.com/us_states/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # get all of the list elements
    li_list = soup.find_all('li')
    for li in li_list:
        p_list = li.find_all('p')

        # get all state names with state capitals
        state_name = p_list[0].text
        state_name = state_name.split(':')[-1].strip()
        state_capital = p_list[1].text
        state_capital = state_capital.split(':')[-1].strip()
        state_capital_long = p_list[2].text
        state_capital_long = state_capital_long.split(':')[-1].strip()
        state_capital_lat = p_list[3].text
        state_capital_lat = state_capital_lat.split(':')[-1].strip()
        print("%s: %s, %s, %s" % (state_name, state_capital, state_capital_long, state_capital_lat))
        #print("%s: %s" % (p_list[0].text, p_list[1].text))

if __name__ == '__main__':
    main()
