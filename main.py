import requests
import pygame
import json





f = open("apikey", "r")
key = f.read()
f.close()
del(f)


# read data from stock api stuffs
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=GOOG&apikey=' + str(key)
del(key)
r = requests.get(url)
data = r.json()

# write data in a nice neat way for me to look at
stored_data = open("data.json", "w")
stored_data.write(json.dumps(data, indent=4))
stored_data.close()

# read weekly data into a dictionary
stored_data = open("data.json", "r")
weekly_data = json.loads(stored_data.read())["Weekly Time Series"]
stored_data.close()

# write only weekly data in a nice neat way for me to look at
weeks = open("weeks.json", "w")
weeks.write(json.dumps(weekly_data, indent=4))
weeks.close()


# get the biggest closing value
biggest = 0
for week in weekly_data.values():
    if float(week["4. close"]) > biggest:
        biggest = float(week["4. close"])

vert_scaling = 5

# actually printing stuff to the pygame window
pygame.init()
screen = pygame.display.set_mode((len(weekly_data), biggest/5))
values = list(weekly_data.values())
values.reverse()
print(values)

for i in range(len(weekly_data)):
    close = values[i]["4. close"]
    pygame.draw.circle(screen, pygame.Color(255, 255, 255), (i, float(close)/5), 1)

# display the stuff we drew
pygame.display.flip()

while True:
    pass
