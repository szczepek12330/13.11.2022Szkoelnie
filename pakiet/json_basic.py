import sys
import json
data= {
    'big_number': 2 ** 3141,
    'max_float': sys.float_info.max,
    'a_list': [2, 3, 5, 7],
}

with open('data1.json', 'w') as json_f:
    json.dump(data, json_f, indent=4, sort_keys=True)

# json_data = json.dumps(data)
# print(json_data)
# data_out = json.loads(json_data)
# print(data_out)
# assert data == data_out

with open('sample.json', 'r') as f:
    data = json.load(f)
print(data)
print(data['members'][2]['powers'][3])