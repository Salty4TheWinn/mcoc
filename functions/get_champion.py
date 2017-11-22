'''Gets a champion from the collection'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return get_champion(event['name'])

def get_champion(name):
    '''Gets a champion from the collection'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        for champ in champions:
            if champ['name'] == name:
                return champ

        return {}