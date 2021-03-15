import json
import praw
from .ocrclient import OCR
from psaw import PushshiftAPI

client_info: object = json.load(open('info.json', 'r'))
client = praw.Reddit(**client_info)
ocr_client: OCR = OCR()
