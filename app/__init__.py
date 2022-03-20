from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from app.utils import Sylviorus

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client


bot = Client("Sylviorus",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             plugins=dict(root="{}/plugins".format(__name__)))


ldb = ("reasons")
mongo_client = MongoClient(MONGO_URI)
SYL = mongo_client.cringe

