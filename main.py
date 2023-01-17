import requests
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import time

if __name__ == "__main__":
  selectors = "game:paper legal:commander -set:sld is:firstprinting"
  api_url = "https://api.scryfall.com/cards/search?&q=year:{0} {1}"
  data = {}
  print("Collecting Data")
  for year in range(1993, datetime.date.today().year):
    response = requests.get(api_url.format(year, selectors))
    response.json()
    data[year] = response.json()["total_cards"]
    time.sleep(random.uniform(0.5, 1.5)) #don't rate limit me bro
  
  print("\nData Collection Finished")
  names = list(data.keys())
  values = list(data.values())
  plt.bar(range(len(data)), values, tick_label=names)
  plt.show()
