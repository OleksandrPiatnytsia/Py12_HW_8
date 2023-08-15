import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
cluster = config.get('DB', 'CLUSTER')
db_name = config.get('DB', 'DBNAME')

URI = f"mongodb+srv://{username}:{password}@{cluster}.hxmjlia.mongodb.net/?retryWrites=true&w=majority"
