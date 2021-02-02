import requests
from typing import Union

OCR_PARAMS: dict = {'lang': '*', 'srv': 'android'}
OCR_BASE: str = 'https://translate.yandex.net/ocr/v1.1/recognize'


class OCR:
    def __init__(self) -> None:
        self.session = requests.session()

    def get_image_bytes(self, uri) -> bytes:
        uri = str(uri)
        if uri.startswith("http"):
            return self.session.get(uri).content
        else:
            return open(uri, "rb").read()
        pass

    def get(self, uri, as_array=False) -> Union[None, list[str], str]:
        bResim: bytes = self.get_image_bytes(uri)
        resim_header: dict = {'file': ('file', bResim, 'image/jpeg')}
        request: requests.Response = self.session.post(OCR_BASE, params=OCR_PARAMS, files=resim_header)
        if request is None:
            print('[abort] request alınamadı')
            return None
        jRequest: dict = request.json()
        print(request.content)
        if 'err' in jRequest:
            print(f'[abort] ocr hata verdi.resp:{jRequest}')
            return None
        texts: list[str] = []
        text: str = ""
        for _ in jRequest['data']['blocks']:
            for __ in _['boxes']:
                if as_array:
                    texts.append(__['text'])
                else:
                    text = __["text"] + '\n'
        if as_array:
            return texts
        else:
            return text.strip()
