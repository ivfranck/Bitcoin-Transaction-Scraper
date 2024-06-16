import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config/config.cfg'))


URL = config.get('scraper', 'url')
_CONNECTION_STRING = config.get('datalake', 'connection_string')
FILE_SYSTEM = config.get('datalake', 'file_system')
DIRECTORY = config.get('datalake', 'directory_name')

