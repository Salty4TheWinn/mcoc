'''Gets all the champions from the collection'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return get_champions()

def get_champions():
    '''Gets all the champions from the collection'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        return champions
