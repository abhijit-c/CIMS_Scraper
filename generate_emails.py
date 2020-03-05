import json

with open('faculty.json', 'r') as f:
    data = json.load(f)

num_faculty = len(data)

for k in range(num_faculty):
    print(data[k]['URL'])
