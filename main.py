account_type = input("Which account are you using? Roth, Traditional, or Main? ").lower()
total_cash = float(input("What is your total investment? $"))
percentage = [.05,.10,.15,.20,.25,.30,.35,.40,.45,.50,.55,.60,.65]
investment_list = {1:"AMZN",2:"BAM", 3:"BRK/B",4:"Cash",5:"DDOG",6:"FTEC",7:"PANW",8:"PLTR",9:"SCHD",10:"IIPR"}

#Only change the keys and index
if account_type == "roth":
  #Below creates a new "sub list" from your investment list which is a dictionary. Therefore you are not indexing but rather using a key to call upon the values. Please always keep this in alphabetical order for neatness
  #Currently pulls AMZN, BAM, BRK/B, Cash, FTEC, PANW, PLTR
  new_investment_list = [investment_list[1],investment_list[2],investment_list[3],investment_list[4],investment_list[6],investment_list[7],investment_list[8]]
  #The investment split will index the percentage list, you only need to change the index when you want to change the portfolios attribution. This also follows the alphabetical order of new investment list
  #Currently pulls: 10%, 10%, 15%, 5%, 50%, 5%, 5%
  investment_split = [total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[2],total_cash*percentage[0],total_cash*percentage[9],total_cash*percentage[0],total_cash*percentage[0]]
  #DO NOT CHANGE!!!! finally we print our calculations this will follow the order we provided above and round to make it currency format. The only time this may change is when you have more or less investments to invest in
  print(f"Invest ${round(investment_split[0],2)} into {new_investment_list[0]}")
  print(f"Invest ${round(investment_split[1],2)} into {new_investment_list[1]}")
  print(f"Invest ${round(investment_split[2],2)} into {new_investment_list[2]}")
  print(f"Invest ${round(investment_split[3],2)} into {new_investment_list[3]}")
  print(f"Invest ${round(investment_split[4],2)} into {new_investment_list[4]}")
  print(f"Invest ${round(investment_split[5],2)} into {new_investment_list[5]}")
  print(f"Invest ${round(investment_split[6],2)} into {new_investment_list[6]}")
elif account_type == "traditional":
  new_investment_list = [investment_list[1],investment_list[2],investment_list[3],investment_list[4],investment_list[6],investment_list[7],investment_list[8]]
  # percentage = [.05,.10,.15,.20,.25,.30,.35,.40,.45,.50,.55,.60,.65]
  investment_split = [total_cash*percentage[2],total_cash*percentage[1],total_cash*percentage[8],total_cash*percentage[0],total_cash*percentage[3],total_cash*percentage[0],total_cash*percentage[0]]
  print(f"Invest ${round(investment_split[0],2)} into {new_investment_list[0]}")
  print(f"Invest ${round(investment_split[1],2)} into {new_investment_list[1]}")
  print(f"Invest ${round(investment_split[2],2)} into {new_investment_list[2]}")
  print(f"Invest ${round(investment_split[3],2)} into {new_investment_list[3]}")
  print(f"Invest ${round(investment_split[4],2)} into {new_investment_list[4]}")
  print(f"Invest ${round(investment_split[5],2)} into {new_investment_list[5]}")
  print(f"Invest ${round(investment_split[6],2)} into {new_investment_list[6]}")
else:
  new_investment_list = [investment_list[1],investment_list[5],investment_list[7],investment_list[8],investment_list[9]]
  investment_split =[total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[11]]
  print(f"Invest ${round(investment_split[0],2)} into {new_investment_list[0]}")
  print(f"Invest ${round(investment_split[1],2)} into {new_investment_list[1]}")
  print(f"Invest ${round(investment_split[2],2)} into {new_investment_list[2]}")
  print(f"Invest ${round(investment_split[3],2)} into {new_investment_list[3]}")
  print(f"Invest ${round(investment_split[4],2)} into {new_investment_list[4]}")

# else:
#   new_investment_list = [investment_list[1],investment_list[5],investment_list[7],investment_list[8],investment_list[9]]
#   investment_split =[total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[1],total_cash*percentage[11]]
#   print(f"Invest ${round(investment_split[0],2)} into {new_investment_list[0]}")
#   print(f"Invest ${round(investment_split[1],2)} into {new_investment_list[1]}")
#   print(f"Invest ${round(investment_split[2],2)} into {new_investment_list[2]}")
#   print(f"Invest ${round(investment_split[3],2)} into {new_investment_list[3]}")
#   print(f"Invest ${round(investment_split[4],2)} into {new_investment_list[4]}")