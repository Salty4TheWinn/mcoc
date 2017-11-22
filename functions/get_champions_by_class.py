'''Gets champions from a given class'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return get_champions_by_class(event['class'])

def get_champions_by_class(class_name):
    '''Gets champions from a given class'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        class_champions = []

        for champ in champions:
            if champ['class'] == class_name:
                class_champions.append(champ)

        return class_champions