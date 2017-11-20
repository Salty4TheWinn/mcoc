'''All functions needed for the backend of MCOC'''
import json

def init_db():
    '''Initialize the JSON file '''

    data = {}
    data['champions'] = []

    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)

def add_champion(name, class_name, rank, stars):
    '''Add a champion to the collection'''
    with open('data.json') as json_data:
        data = json.load(json_data)

        champs = data['champions']

        champ = {}
        stars_data = json.loads(stars)

        champ['name'] = name
        champ['class'] = class_name
        champ['rank'] = rank
        champ['2_Star'] = stars_data[0]
        champ['3_Star'] = stars_data[1]
        champ['4_Star'] = stars_data[2]
        champ['5_Star'] = stars_data[3]
        champs.append(champ)

    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)

    return data
