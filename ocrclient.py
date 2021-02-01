import requests
import config

OCR_PARAMS = {'lang': '*', 'srv': 'android'}
OCR_BASE = 'https://translate.yandex.net/ocr/v1.1/recognize'

class OCR:
    def __init__(self):
        self.session = requests.session()

    def get(self, url,asarray=False):
        bResim = self.session.get(url).content
        resim_header = {'file': ('file', bResim, 'image/jpeg')}
        request = self.session.post(OCR_BASE,params=OCR_PARAMS,files=resim_header)
        if request is None:
            print("[abort] request alınamadı")
            return config.abort
        jRequest = request.json()
        if 'err' in jRequest:
            print(f'[abort] ocr hata verdi.resp:{jRequest}')
            return config.abort
        if asarray:
            texts = []
        else:
            text = ""
        for _ in jRequest['data']['blocks']:
            for __ in _['boxes']:
                if asarray:
                    texts.append(__['text'])
                else:
                    text += f"{__['text']}\n"
        if asarray:
            return texts
        else:
            return text.strip()