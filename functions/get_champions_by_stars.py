'''Gets champions from a given number of stars'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return get_champions_by_stars(event['stars'])

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