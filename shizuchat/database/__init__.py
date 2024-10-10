from pymongo import MongoClient

import config

BADdb = MongoClient(config.MONGO_URL)
BAD = BADdb["BADDb"]["BAD"]


from .chats import *
from .users import *
