import os
import json

with open('tokens.json', 'r') as f:
    tokens = json.load(f)

if not os.path.exists('tokens'):
    os.makedirs('tokens')

for key in tokens.keys():
    filename = key + '.json'
    filepath = os.path.join('tokens', filename)
    with open(filepath, 'w') as f:
        json.dump({key: tokens[key]}, f, indent=2)
