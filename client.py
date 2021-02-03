import json
import praw


client_info = json.load(open("info.json", "r"))
client = praw.Reddit(**client_info)
