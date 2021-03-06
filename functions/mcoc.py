'''All functions needed for the backend of MCOC'''
import json

def init_db():
    '''Initialize the JSON file '''

    data = {}
    data['champions'] = []

    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)

def lambda_handler(event, context):
    return str(event)

def get_champions_by_stars(stars):
    '''Gets champions from a given number of stars'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        star_champions = []

        for champ in champions:
            if champ[stars] is True:
                star_champions.append(champ)

        return star_champions
