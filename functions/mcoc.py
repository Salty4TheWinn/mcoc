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

        champions = data['champions']

        champ = {}
        stars_data = json.loads(stars)

        champ['name'] = name
        champ['class'] = class_name
        champ['rank'] = rank
        champ['2_Star'] = stars_data[0]
        champ['3_Star'] = stars_data[1]
        champ['4_Star'] = stars_data[2]
        champ['5_Star'] = stars_data[3]

        # Check if a champion name already exists:
        for champion in champions:
            if champion['name'] == name:
                return {}

        champions.append(champ)


    with open('data.json', 'w') as json_data:
        json.dump(data, json_data, indent=2)

    return champ

def get_champion(name):
    '''Gets a champion from the collection'''
    with open('data.json') as json_data:
        data = json.load(json_data)
        champions = data['champions']

        for champ in champions:
            if champ['name'] == name:
                return champ

        return {}

def update_champion(name, class_name, rank, stars):
    '''Updates an existing champion in the collection'''

    with open('data.json') as json_data:
        data = json.load(json_data)

        champions = data['champions']
        champ = {}

        # Check if a champion name already exists:
        flag = False

        for champion in champions:
            if champion['name'] == name:
                champ = champion
                flag = True

        if flag is False:
            return {}

        stars_data = json.loads(stars)

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
