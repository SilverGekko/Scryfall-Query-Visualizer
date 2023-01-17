import requests
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import time
import sys

if __name__ == "__main__":
  unique = "game:paper legal:commander -set:sld is:firstprinting"
  selectors = {
    "legends" : "is:commander",
    "expensive" : "usd>=10"
  }
  api_url = "https://api.scryfall.com/cards/search?&q=year:{0} {1} {2}"
  data = {}
  extra = ""
  if len(sys.argv) > 1:
    extra = selectors[sys.argv[1]]
  print("Collecting Data")
  for year in range(1993, datetime.date.today().year):
    print(api_url.format(year, unique, extra))
    response = requests.get(api_url.format(year, unique, extra))
    json_res = response.json()
    if "total_cards" in json_res:
      data[year] = json_res["total_cards"]
    else:
      data[year] = 0
    time.sleep(random.uniform(0.5, 1.5)) #don't rate limit me bro
  
  print("\nData Collection Finished")
  names = list(data.keys())
  values = list(data.values())
  plt.bar(range(len(data)), values, tick_label=names)
  plt.show()
