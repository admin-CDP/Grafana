import json
import random as rd
import datetime 

companies = ['Groupama', 'Coup de Pousse','Fredo','Carrefour']
categories = ['fast_food_restaurants',"hotels_motels_and_resorts","eating_places_restaurants"]


def json_generator(input_json):


    output_json = input_json.copy()
    output_json['data']['object']['amount'] = int(rd.uniform(5,15))
    output_json['data']['object']['card']['cardholder']['company'] = companies[int(rd.uniform(0,4))]
    output_json['created'] = output_json['created'] + int(rd.uniform(-50000000,10))
    output_json['data']['object']['card']['id'] = output_json['data']['object']['card']['id']+str(int(rd.uniform(0,9)))
    output_json['data']['object']["merchant_data"]['category'] = categories[int(rd.uniform(0,3))]
    output_json['Times'] = datetime.datetime.fromtimestamp(output_json['created']).strftime("%m/%d/%Y")


    return output_json


if __name__ == '__main__':

    print('YO')



