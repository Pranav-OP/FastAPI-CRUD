from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "root"
password = "root"
host = "127.0.0.1"
database = "my_database"

engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(username, password, host, database))

base = declarative_base()

session = sessionmaker(bind = engine, expire_on_commit = False)

