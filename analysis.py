# This is simple code, and thus apt to break. srry
import json
from collections import Counter
from datetime import datetime
import calendar
day_of_year = int(datetime.today().strftime('%j'))
current_year = str(datetime.today().strftime("%Y"))


#Counts and Ranks
def counter(value, data):
  list = []
  length = len(data)
  for i in range (length):
    try:
      for item in data[i].keys():
        if item == value:
          list.append(data[i][item])
          list_count = dict(Counter(list))
    except AttributeError:
      print('Offline Song Found -- No Info Available')
      pass 
  sort_list = sorted(list_count.items(), key=lambda x: x[1], reverse=True)
  return sort_list

#Prints Results
def printer(sorted_list, number, criteria, type):
  print('=============***=============')
  if type == 'streaming':
    print(f'\n\n Plays -- {criteria} \n')
    if number == 0:
      for item in sorted_list:
        print(f'{item[1]} -- {item[0]}')
    else:
      for item in sorted_list[:number]:
        print(f'{item[1]} -- {item[0]}')
    print('\n\n')
  elif type == 'playlist':
    print(f'\n\n Plays -- {criteria} \n')
    if number == 0:
      for item in sorted_list:
        print(f'{item[1]} -- {item[0]}')
    else:
      for item in sorted_list[:number]:
        print(f'{item[1]} -- {item[0]}')
    print('\n\n')

#Processes Streaming
def streaming():
  with open('StreamingHistory0.json',encoding="UTF8") as f:
    data = json.load(f)
  time_data = []

  print(f'Sort By: \n\n'
  f'~# 1  --  Artist \n'
  f'~# 2  --  Track  \n\n')
  choice = (input('~# '))

  print(f'Time Frame: \n\n'
  f'~# 1  --  Search the Past Year\n'
  f'~# 2  --  Search the Past Month\n'
  f'~# 3  --  Search by Specific Month\n\n')
  time_choice = (input('~# '))
  if time_choice == '3':
    month_input = (input('Enter in the MM as YYYY-MM (include the dash) ::  '))
  for item in data:
    y = datetime.strptime(item['endTime'], "%Y-%m-%d %H:%M").date()
    year_day = int(y.strftime("%j"))
    year_month = y.strftime("%Y-%m")
    if time_choice == '1':
      time_data.append(item)

    elif time_choice == '2':
      if (day_of_year >= year_day >= (day_of_year-40)) and(y.strftime("%Y") == current_year):
        time_data.append(item)
    elif time_choice == '3':
      if month_input == year_month:
        time_data.append(item)     

  if choice == '1': 
    print('------*------')  
    print('How many results do you want?\n'
    f'Enter "0" for ALL; Otherwise input a number \n')
    num = int(input('~# '))
    print('Hacking....\n\n')
    printer(counter('artistName', time_data), num, 'Artist', 'streaming')
  elif choice == '2':
    print('------*------')
    print('How many results do you want?\n'
    f'Enter "0" for ALL; Otherwise input a number \n')
    num = int(input('~# '))
    print('Hacking....\n\n')
    printer(counter('trackName', time_data), num, 'Track', 'streaming')    

        

#Retrieves Requested Playlist
def playlist_grabber():
  with open('Playlist1.json',encoding="UTF8") as f:
    data1 = json.load(f)
  data = []
  data.append(data1)
  try:
    with open('Playlist2.json',encoding="UTF8") as g:
      data2 = json.load(g)
    data.append(data2)
  except:
    pass
  try:
    with open('Playlist3.json',encoding="UTF8") as h:
      data3 = json.load(h)
    data.append(data3)
  except:
    pass
  
  count = 0
  for i in range (2):
    for item in data[i].keys():
      for entry in data[i][item]:
        print(f"~#{count} -- {entry['name']}")
        count += 1
  rep = True
  while rep == True:     
    print('\n ---------------------------------------- \n')
    print('Please choose a playlist number, or type 000 for ALL')
    playlist_input = int(input('~# '))
    
    try:
      if playlist_input == 000:
        list = data[0]['playlists'][:] + data[1]['playlists'][:]
        rep = False
        return list
      else:
        try:
          return data[0]['playlists'][playlist_input]
          rep = False
        except:
          try:
            return data[1]['playlists'][playlist_input-len(data[0]['playlists'][:])]
            rep = False
          except:
            return data[2]['playlists'][playlist_input-(len(data[0]['playlists'][:])+len(data[1]['playlists'][:]))]
    except:
      print('\n*** Invalid Playlist Number ***\n')
      rep = True

#Processes the Playlist
def playlist():
  value = playlist_grabber()
  playlist_list = []
  check = True
  try:
  
    for item in value['items']:
      try:
        playlist_list.append(item['track'])
        
      except TypeError:
        
        playlist_list.append('** LOCAL SONG -- INFO UNAVAILABLE **')
  except:
    for item in value:
      
      for title in item['items']:
        try:
          playlist_list.append(title['track'])
          
        except TypeError:
          
          playlist_list.append('** LOCAL SONG -- INFO UNAVAILABLE **')
          
  while check == True:
    print('------------------------')
    print(f'Sort By: \n\n'
    f'~# 1  --  Artist \n'
    f'~# 2  --  Track  \n'
    f'~# 3  --  Albums \n\n')

    while check1 == True:
      try:
        choice = int(input('~# '))
        if choice == 1: 
          print('\n------*------')  
          print('How many results do you want?\n'
          f'Enter "0" for ALL; Otherwise input a number \n')
          num = int(input('~# '))
           
          print('Hacking....\n\n')
          printer(counter('artistName', playlist_list), num, 'Artist', 'playlist')
        elif choice == 2:
          print('\n------*------')
          print('How many results do you want?\n'
          f'Enter "0" for ALL; Otherwise input a number \n')
          num = int(input('~# '))
          
          print('Hacking....\n\n')
          printer(counter('trackName', playlist_list), num, 'Track', 'playlist')
          #pass
        elif choice == 3:
          print('\n------*------')
          print('How many results do you want?\n'
          f'Enter "0" for ALL; Otherwise input a number \n')
          num = int(input('~# '))
          
          print('Hacking....\n\n')
          printer(counter('albumName', playlist_list), num, 'Album', 'playlist')
        elif isinstance(choice, int) == False:
          print('Enter a Number')
          
        else:
          print(f'{choice} is invalid')
          
      except:
        print('No. ')
        
    check = False

#MAIN
def main():
  repeat = True
  while repeat == True:
    print(f'========**===============**========\n'
    f'\t\tSpotify Looker-Atter\n'
    f'========**===============**======== \n\n'
    f'~# 1  --  Streaming History \n'
    f'~# 2  --  Playlist Insight  \n')
    check = True
 
      while check == True:
          user = (input('~# '))
          if user == '1':
            streaming()
            check = False
          elif user == '2':
            playlist()
            check = False
          else:
            print('Please enter a 1 or 2')
            check = True

    print('-------------------------------------')
    print('Finished and/or Crashed! Would you like to run again? (Y / N)')
    rep = input(':: ')
    if rep.lower() == 'y':
      repeat = True
    else:
      repeat = False
  

main()

