from ocrclient import OCR
from client import client

#Returns: Post


def find_post(image_url):
    ocr_client = OCR()
    yazi = ocr_client.get(image_url, asarray=True)
    full = " ".join(yazi)
    matches = []
    matchnums = []
    truematch = None
    for yaziblok in yazi[1:-1]:
        print("[UYARI]", yaziblok)
        try:
            wordbyword = yaziblok.split()
            if len(wordbyword) <= 1 or "comments" in wordbyword or (
                    any(listing in wordbyword for listing in ["best", "hot", "new"]) and len(
                    wordbyword) == 1) or yaziblok.strip("1234567890") == "":
                continue
            yaziblok = yaziblok.strip("1234567890")
            search = client.subreddit("all").search(yaziblok)
            notmatched = False
            for result in search:
                title = result.title
                for kelime in title:
                    if kelime not in full:
                        notmatched = True
                if notmatched:
                    continue
                matches.append(result)
                print(result)
        except:
            continue
    for match in matches:
        length = len(match.title)
        matchnums.append(length)
        if length == max(matchnums):
            truematch = match
    matches.remove(truematch) #just to be safe idk that much python
    return truematch
