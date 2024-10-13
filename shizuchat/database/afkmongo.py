from typing import Dict, Union

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from config import MONGO_URL

mongo = MongoCli(MONGO_URL)
db = mongo.shizuchat

afkdb = db.afk
