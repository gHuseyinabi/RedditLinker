import logging
import requests
from typing import Iterable, Union

OCR_PARAMS: dict = {'lang': '*', 'srv': 'android'}
OCR_BASE: str = 'https://translate.yandex.net/ocr/v1.1/recognize'


class OCR:
    def __init__(self):
        self.session = requests.session()

    def get_image_bytes(self, uri):
        uri = str(uri)
        if uri.startswith('http'):
            return self.session.get(uri).content
        else:
            return open(uri, 'rb').read()
        pass

    def get(self, uri, as_array=False):
        bResim = self.get_image_bytes(uri)
        resim_header = {'file': ('file', bResim, 'image/jpeg')}
        request: requests.Response = self.session.post(OCR_BASE, params=OCR_PARAMS, files=resim_header)
        if request is None:
            logging.error('request alınamadı')
            return None
        jRequest = request.json()
        if 'err' in jRequest:
            logging.error(f'ocr hata verdi.resp:{jRequest}')
            return None
        texts = []
        text = ''
        for Block in jRequest['data']['blocks']:
            for Box in Block['boxes']:
                if as_array:
                    texts.append(Box['text'])
                else:
                    text = Box['text'] + '\n'
        if as_array:
            return texts
        else:
            return text.strip()
