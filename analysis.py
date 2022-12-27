# This is simple code, and thus apt to break. srry
import json
from collections import Counter
from datetime import datetime
import calendar
import glob
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
def printer(sorted_list, number, criteria, type, time):
    print('=============***=============')
    if type == 'streaming':
        print(f'\n\n Plays -- {criteria} \n')
        if number == 0:
            for item in sorted_list:
                print(f'{item[1]} -- {item[0]}')
            print(f'\nTIME: {time:,} minutes')
        else:
            for item in sorted_list[:number]:
                print(f'{item[1]} -- {item[0]}')
            print(f'\nTIME: {time:,} minutes')
        print('\n')
    elif type == 'playlist':
        print(f'\n\n Plays -- {criteria} \n')
        if number == 0:
            for item in sorted_list:
                print(f'{item[1]} -- {item[0]}')
        else:
            for item in sorted_list[:number]:
                print(f'{item[1]} -- {item[0]}')
        print('\n')

#Processes Streaming
def streaming():
    directory = 'MyData'
    time_meta = 'msPlayed'
    data = []
    # Converts JSON into dict, stores in  list
    for filename in glob.iglob(f'{directory}/StreamingHistory*.json'):
        with open(filename, encoding="UTF-8") as f:
            filenames = json.load(f)
            data.append(filenames)
    
    time_data = []
    summary_data = {}
    print(f'Sort By: \n\n'
    f'~# 1  --  Artist \n'
    f'~# 2  --  Track\n\n')

    choice = (input('~# '))
    if choice == '1':
        criteria = ('artistName', 'Artist')
    elif choice == '2':
        criteria = ('trackName', 'Track')
    else:
        print('Wrong Answer!')
        return
    print(f'Time Frame: \n\n'
    f'~# 1  --  Search the Past Year\n'
    f'~# 2  --  Search the Past Month\n'
    f'~# 3  --  Search by Specific Month\n'
    f'~# 4  --  Search only {current_year}\n'
    f'~# 5  --  Monthly Summary\n\n')
    time_choice = (input('~# '))
    if time_choice == '3':
        month_input = (input('Enter in the MM as YYYY-MM (include the dash)::  '))
        months = {'01':[],'02':[],'03':[],'04':[],'05':[],'06':[],'07':[],'08':[],'09':[],'10':[],'11':[],'12':[]}
    elif time_choice == '1' or time_choice == '2' or time_choice == '4' or time_choice == '5':
        pass
    else:
        print('Wrong answer!')
        return

    streaming_length = (len(data))
    for i in range(streaming_length):       # Starts iterating through Streaming
        for item in data[i]:            # Each streaming song is a data[i] 
            y = datetime.strptime(item['endTime'], "%Y-%m-%d %H:%M").date() # Forces data into standard format
            year_day = int(y.strftime("%j"))
            year_month = y.strftime("%Y-%m")
            stream_month = y.strftime("%m")
         
            if time_choice == '1':
                time_data.append(item)
            elif time_choice == '2':
                if (day_of_year >= year_day >= (day_of_year-40)) and (y.strftime("%Y") == current_year):
                    time_data.append(item)
                    
            elif time_choice == '3':
                if month_input == year_month:
                    time_data.append(item)       
            
            elif time_choice == '4':
                if y.strftime("%Y") == current_year:
                    time_data.append(item)
            
            elif time_choice == '5':
                if stream_month not in summary_data.keys():
                    summary_data[stream_month] = [item]
                else:
                    summary_data[stream_month].append(item)
    print('------*------')
    print('How many results do you want?\n')
    f'Enter "0" for ALL; Otherwise input a number \n'
    num = int(input('~# '))
    print('Hacking....\n\n')
    if time_choice == '5':
        sumsort = {key:summary_data[key] for key in sorted(summary_data.keys())}
        for every_month in sumsort.keys():
            month_name = datetime.strptime(every_month, "%m").strftime("%B")
            printer(counter(criteria[0], sumsort[every_month]), num, month_name, 'streaming',time_calc(sumsort[every_month], time_meta))
    else:
        printer(counter(criteria[0], time_data), num, criteria[1], 'streaming', time_calc(time_data, time_meta))

# Calculates total time listened 
def time_calc(time_data, time_meta):
    time_tuples  = counter(time_meta, time_data)
    time_multiplied = []
    for i in range(len(time_tuples)):
        multiplied = time_tuples[i][0] * time_tuples[i][1]
        time_multiplied.append(multiplied)
    time_ms = sum(time_multiplied)
    time_listened = time_ms // 1000 // 60
    return time_listened

def streaming_ext():
    directory = 'MyDataExtended'
    time_meta = 'ms_played'
    data = []
    # Converts JSON into dict, stores in list
    for filename in glob.iglob(f'{directory}/endsong*.json'):
        with open(filename, encoding="UTF-8") as w:
            filenames = json.load(w)
            data.append(filenames)

    time_data = []
    summary_data = {}

    print(f'Sort By: \n\n'
    f'~# 1  --  Artist \n'
    f'~# 2  --  Track  \n'
    f'~# 3  --  Album  \n\n')
    choice = (input('~# '))
    if choice == '1':
        criteria = ('master_metadata_album_artist_name', 'Artist')
    elif choice == '2':
        criteria = ('master_metadata_track_name', 'Track')
    elif choice == '3':
        criteria = ('master_metadata_album_album_name', 'Album')
    else:
        print('Wrong answer!')
        return

    print(f'Time Frame: \n\n'
    f'~# 1  --  Search All of Time\n'
    f'~# 2  --  Search by Month\n'
    f'~# 3  --  Search Month + Specific Year\n'
    f'~# 4  --  Search Specific Year\n'
    f'~# 5  --  Yearly Summary\n\n')
    time_choice = (input('~# '))
    if time_choice == '3':
        month_input = (input('Enter as YYYY-MM (include the dash) ::  '))
    elif time_choice == '2':
        month_input = (input('Enter as MM ::  '))
    elif time_choice == '4':
        year_input = (input('Enter as YYYY  ::  '))
    elif time_choice == '1' or time_choice == '5':
        pass
    else:
        print('Wrong answer!')
        return
    streaming_length = (len(data))
    

    for i in range(streaming_length):       # Starts iterating through Streaming
        for item in data[i]:            # Each streaming song is a data[i] or item
            y = datetime.strptime(item['ts'], "%Y-%m-%dT%H:%M:%SZ").date() # Forces data into standard format
            year_day = int(y.strftime("%j"))
            year_month = y.strftime("%Y-%m")
            stream_month = y.strftime("%m")
            stream_year = y.strftime("%Y") 
            
            if time_choice == '1':
                time_data.append(item)

            elif time_choice == '2':
                if month_input == stream_month:
                    time_data.append(item)

            elif time_choice == '3':
                if month_input == year_month:
                    time_data.append(item)       
            
            elif time_choice == '4':
                if year_input == stream_year:
                    time_data.append(item)
            elif time_choice == '5':
                if stream_year not in summary_data.keys():
                    summary_data[stream_year] = [item]
                else:
                    summary_data[stream_year].append(item)
    print('------*------')
    print('How many results do you want?\n')
    f'Enter "0" for ALL; Otherwise input a number \n'
    num = int(input('~# '))
    print('Hacking....[this may take some time]\n\n')
    if time_choice == '5':
        sumsort = {key:summary_data[key] for key in sorted(summary_data.keys())}
        for every_year in sumsort.keys():
            printer(counter(criteria[0], sumsort[every_year]), num, every_year, 'streaming',time_calc(sumsort[every_year], time_meta))
    else:
        printer(counter(criteria[0], time_data), num, criteria[1], 'streaming',time_calc(time_data, time_meta))              

#Retrieves Requested Playlist
def playlist_grabber():
    directory = 'MyData'
    data = []
    # Converts JSON into dict, stores in  list
    for filename in glob.iglob(f'{directory}/Playlist*.json'):
        with open(filename, encoding="UTF-8") as f:
            filenames = json.load(f)
            data.append(filenames)
    time_data = []
       
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
                    

    print('------------------------')
    print(f'Sort By: \n\n'
    f'~# 1  --  Artist \n'
    f'~# 2  --  Track  \n'
    f'~# 3  --  Albums \n\n')
    try:
        choice = int(input('~# '))
        if choice == 1: 
            print('\n------*------')    
            print('How many results do you want?\n'
            f'Enter "0" for ALL; Otherwise input a number \n')
            num = int(input('~# '))
                
            print('Hacking....\n\n')
            printer(counter('artistName', playlist_list), num, 'Artist', 'playlist', 0)
        elif choice == 2:
            print('\n------*------')
            print('How many results do you want?\n'
            f'Enter "0" for ALL; Otherwise input a number \n')
            num = int(input('~# '))
            
            print('Hacking....\n\n')
            printer(counter('trackName', playlist_list), num, 'Track', 'playlist', 0)
            #pass
        elif choice == 3:
            print('\n------*------')
            print('How many results do you want?\n'
            f'Enter "0" for ALL; Otherwise input a number \n')
            num = int(input('~# '))
            
            print('Hacking....\n\n')
            printer(counter('albumName', playlist_list), num, 'Album', 'playlist', 0)
        elif isinstance(choice, int) == False:
            print('Enter a Number')
            
        else:
            print(f'{choice} is invalid')
            
    except:
        print('No. ')
                

#MAIN
def main():
    repeat = True
    while repeat == True:
        print(f'========**===============**========\n'
        f'\tSpotify Looker-Atter\n'
        f'========**===============**======== \n\n'
        f'~# 1  --  Account Data \n'
        f'~# 2  --  Extended Streaming History\n'
        f'~# 3  --  Playlist Insight \n')
        check = True
 
        while check == True:
                user = (input('~# '))
                if user == '1':
                    print('****  Please make sure your data is in a folder titled "MyData"')
                    streaming()
                    check = False
                elif user == '2':
                    print('****  Please make sure your data is in a folder titled "MyDataExtended"')
                    streaming_ext()
                    check = False
                elif user == '3':
                    print('****  Please make sure your data is in a folder titled "MyData"')
                    playlist()
                    check = False
                else:
                    print('Please enter a 1 or 2 or 3')
                    check = True

        print('-------------------------------------')
        print('Finished and/or Crashed! Would you like to run again? (Y / N)')
        rep = input(':: ')
        if rep.lower() == 'y':
            repeat = True
        else:
            repeat = False
    

main()
