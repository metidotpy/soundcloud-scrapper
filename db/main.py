from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Table, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os


class DB:
    def create(self, path ,name):
        if name.endswith('.db'):
            self.engine = create_engine(f"sqlite:///{os.path.join(path, name)}")
        else:
            self.engine = create_engine(f"sqlite:///{os.path.join(path, name+'.db')}")
        self.meta = MetaData()
        self.Session = sessionmaker(bind=self.engine)()
        
        return self.engine, self.meta, self.Session

    def create_table(self):
        self.urls = Table(
            'urls',self.meta,
            Column('id', Integer, unique=True, primary_key=True, autoincrement=True, nullable=False),
            Column('url', String, nullable=False),
        )
        self.meta.create_all(self.engine)
    
    def create_table_iframes(self):
        self.iframes = Table(
            'iframes', self.meta,
            Column('id', Integer, unique=True, primary_key=True, autoincrement=True, nullable=False),
            Column('url', String, nullable=False),
            Column('name', String, nullable=False),
            Column('author', String, nullable=False),
            Column('author_link', String, nullable=False),
            Column('iframe', String, nullable=False),
        )
        self.meta.create_all(self.engine)
    
    def insert_data(self, url):
        self.engine.execute(self.urls.insert(), url=url)
        if len(url) > 20:
            print("{0}... added to database".format(url[:21]))
        else:
            print("{0} added to database".format(url))
    
    def insert_data_iframes(self, url, name, author, author_link, iframe):
        self.engine.execute(self.iframes.insert(), url=url, name=name, author=author, author_link=author_link, iframe=iframe)

        if len(iframe) > 20:
            print("{0}... added to database".format(iframe[:21]))
        else:
            print("{0} added to database".format(iframe))

database = DB()