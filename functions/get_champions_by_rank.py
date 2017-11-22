'''Gets champions from a given rank'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return get_champions_by_rank(event['rank'])

def get_champions_by_rank(rank):
    '''Gets champions from a given rank'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        rank_champions = []

        for champ in champions:
            if champ['rank'] == rank:
                rank_champions.append(champ)

        return rank_champions