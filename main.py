import json
from operations import Operations


with open('operations.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    for item in json_data:
        if 'date' not in item:
            item['date'] = ''
    sorted_json = sorted(json_data, key=lambda x: x['date'], reverse=True)

    counter = 0

    for i in sorted_json:
        if counter == 5:
            break
        if i['state'] == 'EXECUTED':
            counter += 1
        else:
            continue
        class_sorted_jason = Operations(i)
        print(class_sorted_jason.info())
        print("")