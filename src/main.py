import requests
import pygame
import json
from extensions import Graph
import time




f = open("src/apikey", "r")
key = f.read()
f.close()
del(f)


# read data from stock api stuffs
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=GOOG&apikey=' + str(key)
del(key)
r = requests.get(url)
data = r.json()

# write data in a nice neat way for me to look at
stored_data = open("src/data/data.json", "w")
stored_data.write(json.dumps(data, indent=4))
stored_data.close()

# read weekly data into a dictionary
stored_data = open("src/data/data.json", "r")
weekly_data = json.loads(stored_data.read())["Weekly Adjusted Time Series"]
stored_data.close()

# write only weekly data in a nice neat way for me to look at
weeks = open("src/data/weeks.json", "w")
weeks.write(json.dumps(weekly_data, indent=4))
weeks.close()



# get the biggest closing value
biggest = 0
for week in weekly_data.values():
    if float(week["5. adjusted close"]) > biggest:
        biggest = float(week["5. adjusted close"])

stock_graph = Graph(5, 3, 0, 0)


# make da screen
pygame.init()
screen = pygame.display.set_mode((stock_graph.HORIZONTAL_SCALING * len(weekly_data) + stock_graph.horizontal_offset, biggest * stock_graph.VERT_SCALING + stock_graph.vert_offset))
pygame.display.set_caption("fwancy gwaph")
pygame.display.set_icon(pygame.image.load("src/assets/icon.png"))
stock_graph.set_display(pygame.display)

values = list(weekly_data.values())
values.reverse()


# actually printing stuff to the pygame window
for i in range(len(weekly_data)):
    # pygame needs to constantly interact with the os or something idk
    pygame.event.get()

    close = values[i]["5. adjusted close"]
    pygame.draw.circle(screen, pygame.Color(255, 255, 255), stock_graph.get_coords(i, float(close)), 1)
    
    # display the stuff we drew fancily
    pygame.display.flip()
    time.sleep(0.002)
    
time.sleep(5)


"""
text in pygame

https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

"""