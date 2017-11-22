'''Removes a champion from the collection'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return remove_champion(event['name'])

def remove_champion(name):
    '''Removes a champion from the collection'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        for champ in champions:
            if champ['name'] == name:
                champions.remove(champ)
                with open('data.json', 'w') as json_data:
                    json.dump(data, json_data, indent=2)
                return champ

        return {}
