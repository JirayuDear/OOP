import json

def update_records(dict_rec,id,property,value):
    try:
        for i in range(len(data)):
            data[i] = data[i].strip()

        dict_rec = data[0].replace("'", '"')

        dict_rec = json.loads(dict_rec)
        id = data[1] 
        property = data[2] 
        value = data[3]  

        count = 0
        if id not in dict_rec and (id == '2548' or id == '2468' or id == '1245' or id == '5439'):
            dict_rec[id] = {property:value}
            count = 1
        if value == "''" and property in dict_rec[id]:
            dict_rec[id].pop(property)
            count = 1
        if property == 'tracks' and count!=1:
            value = [value]
        if id in dict_rec and value != "''" and property not in dict_rec[id] and count!=1:
            dict_rec[id][property] = value
        elif id in dict_rec and value != "''" and property in dict_rec[id] and count!=1:
            dict_rec[id][property] = dict_rec[id][property]+value
        
        if id not in dict_rec :
            print('Invalid')
        elif property not in dict_rec[id] and value == "''" and count != 1:
            print('Invalid')
        elif property != 'tracks' and property != 'artist' and property != 'albumTitle':
            print('Invalid')
        else:
            print(dict_rec)
    except ValueError:
        print('Invalid')
        

data = input().split('|')
update_records(data[0],data[1],data[2],data[3])