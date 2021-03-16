import json
import praw
from .ocrclient import OCR

client_info = json.load(open('info.json', 'r'))
client = praw.Reddit(**client_info)
ocr_client = OCR()
