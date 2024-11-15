import socket
import time

import heroku3
from pyrogram import filters

import config
from shizuchat.database.mongo import pymongodb


SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    "https",
    "HEAD",
    "main",
]


def dbb():
    global db
    global clonedb
    db = {}
    clonedb = {}
    LOGGER(__name__).info(f"Database Initialized.")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            SUDOERS.add(user_id)
    else:
        sudoersdb = pymongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        for user_id in OWNER:
            SUDOERS.add(user_id)
            if user_id not in sudoers:
                sudoers.append(user_id)
                sudoersdb.update_one(
                    {"sudo": "sudo"},
                    {"$set": {"sudoers": sudoers}},
                    upsert=True,
                )
        if sudoers:
            for x in sudoers:
                SUDOERS.add(x)
    LOGGER(__name__).info(f"Sudoers Loaded.")
