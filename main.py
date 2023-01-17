import requests
import matplotlib.pyplot as plt
import numpy as np
import random
import datetime
import time
import sys

if __name__ == "__main__":
  today_year = datetime.date.today().year
  main_selectors = "game:paper legal:commander -set:sld"
  selectors = {
    "legends" : "is:commander",
    "expensive" : "usd>=10",
    "commander" : "settype:commander",
    "standard" : "settype:standard"
  }
  api_url = "https://api.scryfall.com/cards/search?&q=year:{0} {1} {2} {3}"
  data = {}
  extra_selectors = ""
  unique_or_reprint = "is:firstprinting"
  if len(sys.argv) > 1:
    extra_selectors = selectors[sys.argv[1]]
  if sys.argv[-1:]:
    unique_or_reprint = "is:reprint"
  print("Collecting Data")
  for year in range(1993, today_year):
    formatted_query = api_url.format(year, main_selectors, extra_selectors, unique_or_reprint)
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
  plt.xlabel('Amount')
  plt.ylabel('Year')
  plt.title("/cards/search?&q=year:{0} {1} {2} {3}".format("1993-" + str(today_year), main_selectors, extra_selectors, unique_or_reprint))
  f = plt.figure(num=1)
  f.set_figwidth(20)
  f.set_figheight(8)
  plt.bar(range(len(data)), values, tick_label=names)
  plt.show()
