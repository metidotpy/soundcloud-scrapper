from db.main import database
from json_.main import json_

class CreateAll():
    def all(self, path, name, datas):
        json_.insert_data(path=path, name=name, data=datas)
        database.create(path=path, name=name)
        database.create_table()
        for data in datas:
            database.insert_data(url=data)
    
    def all_iframe(self, path, name, datas:dict):
        json_.insert_data(path=path, name=name, data=datas)
        database.create(path=path, name=name)
        database.create_table_iframes()
        for key, value in datas.items():
            url = key
            name = value[0]
            author = value[1]
            author_link = value[2]
            iframe = value[3]
            database.insert_data_iframes(url=url, name=name, author=author, author_link=author_link, iframe=iframe)

create_all = CreateAll()