'''Updates an existing champion in the collection'''
import json

def lambda_handler(event, context):
    '''Handler of the function'''
    return update_champion(event['name'], event['class'], event['rank'], [event['2_Star'], event['3_Star'], event['4_Star'], event['5_Star']])

def update_champion(name, class_name, rank, stars):
    '''Updates an existing champion in the collection'''

    with open('data.json') as json_data:
        print("HOLA")
        data = json.load(json_data)

        champions = data['champions']
        champ = {}

        print("HOLA")

        # Check if a champion name already exists:
        flag = False

        for champion in champions:
            if champion['name'] == name:
                champ = champion
                flag = True

        if flag is False:
            return {}

        print("HOLA")

        stars_data = stars

        print("HOLA")

        champ['name'] = name
        champ['class'] = class_name
        champ['rank'] = rank
        champ['2_Star'] = stars_data[0]
        champ['3_Star'] = stars_data[1]
        champ['4_Star'] = stars_data[2]
        champ['5_Star'] = stars_data[3]

    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)

    return champ