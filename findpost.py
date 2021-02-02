from ocrclient import OCR
from client import client


def find_post(image_url) -> dict:
    ocr_client: OCR = OCR()
    yazi = ocr_client.get(image_url, as_array=True)
    print(yazi)
    full = " ".join(yazi)
    matches = []
    matchnums = []
    truematch = None
    for yaziblok in yazi[1:]:
        print("[UYARI]", yaziblok)
        try:
            wordbyword = yaziblok.split()
            if len(wordbyword) <= 1 or "comments" in wordbyword or (
                    any(listing in wordbyword for listing in ["best", "hot", "new"]) and len(
                    wordbyword) == 1) or yaziblok.strip("1234567890") == "":
                continue
            #çok ayrıntılı bir arama
            for advkelime in wordbyword:
                if advkelime[0].isdigit() and (advkelime.endswith("k")  or advkelime.endswith(".")):
                    yaziblok = yaziblok.replace(advkelime,"")
            yaziblok = yaziblok.strip()
            print("Filtered:",yaziblok)
            search = client.subreddit("all").search(yaziblok)
            notmatched = False
            foundany = False
            for result in search:
                title = result.title
                directaccess = False
                if title == yaziblok:
                    directaccess = True
                if not directaccess:
                    for kelime in title:
                        if kelime not in full:
                            notmatched = True
                    if notmatched:
                        continue
                foundany = True
                matches.append(result)
                print(f"Found one!The name is {result.title} and the url is https://www.reddit.com{result.permalink}")
            if foundany:
                break
        except Exception as e:
            print(e)
            continue
    for match in matches:
        length = len(match.title)
        matchnums.append(length)
        if length == max(matchnums):
            truematch = match
    return {"match": truematch, "matches": matches}
