import os
import json

folder_path = 'tokens'
i = 1
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path) as f:
            data = json.load(f)
        
        for key, value in data.items():
            name = value.get('NAME')
            if name is not None:
                if isinstance(name, list):
                    name_text = ''.join([chr(x) for x in name])
                else:
                    name_text = str(name)
                
                print(f"{i}. {key}: {name_text}")
            elif (name == None) or (len(name) == []):
                print(f"{i}. {key}: ")
    i = i + 1
