import json
import os

class Json:
    def insert_data(self, path, name, data):
        if name.endswith('.json'):
            with open(os.path.join(path, name), 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            with open(os.path.join(path, name+'.json'), 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
    
    def read_data(self, path, name):
        if name.endswith('.json'):
            with open(os.path.join(path, name), 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                return data
        else:
            with open(os.path.join(path, name+'.json'), 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                return data
json_ = Json()