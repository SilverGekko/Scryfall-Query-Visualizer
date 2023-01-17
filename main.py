import requests
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import time
import sys

if __name__ == "__main__":
  unique = "game:paper legal:commander -set:sld"
  selectors = {
    "legends" : "is:commander",
    "expensive" : "usd>=10",
    "commander" : "settype:commander",
    "standard" : "settype:standard"
  }
  api_url = "https://api.scryfall.com/cards/search?&q=year:{0} {1} {2} {3}"
  data = {}
  extra = ""
  unique_or_reprint = "is:firstprinting"
  if len(sys.argv) > 1:
    extra = selectors[sys.argv[1]]
  if len (sys.argv) > 2:
    unique_or_reprint = "is:reprint"
  print("Collecting Data")
  for year in range(1993, datetime.date.today().year):
    formatted_query = api_url.format(year, unique, unique_or_reprint, extra)
    print(formatted_query)
    response = requests.get(formatted_query)
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
