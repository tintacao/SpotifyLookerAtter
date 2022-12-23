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

#Processes Streaming
def streaming():
    directory = 'MyData'
    data = []
    # Converts JSON into dict, stores in list
    for filename in glob.iglob(f'{directory}/endsong*.json'):
        with open(filename, encoding="UTF-8") as w:
            filenames = json.load(w)
            data.append(filenames)

    time_data = []

    print(f'Sort By: \n\n'
    f'~# 1  --  Artist \n'
    f'~# 2  --  Track  \n'
    f'~# 3  --  Album  \n\n')
    choice = (input('~# '))

    print(f'Time Frame: \n\n'
    f'~# 1  --  Search All of Time\n'
    f'~# 2  --  Search by Month\n'
    f'~# 3  --  Search Month + Specific Year\n'
    f'~# 4  --  Search Specific Year\n\n')
    time_choice = (input('~# '))
    if time_choice == '3':
        month_input = (input('Enter as YYYY-MM (include the dash) ::  '))
    elif time_choice == '2':
        month_input = (input('Enter as MM ::  '))
    elif time_choice == '4':
        year_input = (input('Enter as YYYY  ::  '))
    streaming_length = (len(data))
    

    for i in range(streaming_length):       # Starts iterating through Streaming
        for item in data[i]:            # Each streaming song is a data[i] 
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
 
    def time_calc(time_data):
        time_tuples  = counter('ms_played', time_data)
        time_multiplied = []
        for i in range(len(time_tuples)):
            multiplied = time_tuples[i][0] * time_tuples[i][1]
            time_multiplied.append(multiplied)
        time_ms = sum(time_multiplied)
        time_listened = time_ms // 1000 // 60
        return time_listened
    print('------*------')
    print('How many results do you want?\n')
    f'Enter "0" for ALL; Otherwise input a number \n'
    num = int(input('~# '))
    print('Hacking....[this may take some time]\n\n')
    if time_choice == '5':
        month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_data = list(months.values())
        count = 0
        if choice == '1': 
            for every_month in month_name:
                time_data = month_data[count]
                printer(counter('master_metadata_album_artist_name', time_data), num, every_month, 'streaming',time_calc(time_data))
                count+=1
        elif choice == '2':
            for every_month in month_name:
                time_data = month_data[count]
                printer(counter('master_metadata_track_name', time_data), num, every_month, 'streaming',time_calc(time_data))
                count+=1
    else:
        if choice == '1':
            printer(counter('master_metadata_album_artist_name', time_data), num, 'Artist', 'streaming',time_calc(time_data))
        elif choice == '2':
            printer(counter('master_metadata_track_name', time_data), num, 'Track', 'streaming',time_calc(time_data))
        elif choice == '3':
            printer(counter('master_metadata_album_album_name', time_data), num, 'Album', 'streaming',time_calc(time_data))              

#MAIN
def main():
    repeat = True
    while repeat == True:
        print(f'========**===============**========\n'
        f'\tSpotify Looker-Atter\n'
        f'========**===============**======== \n\n'
        f'EXTENDED STREAMING HISTORY\n\n'
        f'Please make sure that the folder with your Account History is named "MyData" and is in the same folder as this file\n')
        
        streaming()

        print('-------------------------------------')
        print('Finished and/or Crashed! Would you like to run again? (Y / N)')
        rep = input(':: ')
        if rep.lower() == 'y':
            repeat = True
        else:
            repeat = False
    

main()
