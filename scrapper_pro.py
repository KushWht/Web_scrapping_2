from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(START_URL)

soup = bs(page.text, "html.parser")
star_table = soup.find_all('table')

temp_list = []
table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][0])
    mass.append(temp_list[i][0])
    radius.append(temp_list[i][0])

df2 = pd.DataFrame(list(zip(star_name, distance, mass, radius)), columns=["Star Name", "Distance", "Mass", "Radius"])
print(df2)

df2.to_csv('star.csv')