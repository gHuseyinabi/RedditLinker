from client import client, ocr_client
import logging
poop_words = {
    'multi': [
        "comments",
        "Posted by"
    ],
    'single': [
        "best",
        "how",
        "new"
    ]
}


def SafeIndex(arr, index):
    try:
        return arr[index]
    except:
        return ""


def check_skippable_query(query: list[str], full: str) -> bool:
    if full.strip("1234567890 ") == "":
        return True
    if any(poop_word == full for poop_word in poop_words['single']):
        return True
    if any(poop_word in query for poop_word in poop_words['multi']):
        logging.info("User may be " + SafeIndex(query, 2))
        return True
    if len(query) <= 1:
        return True


def find_post(image_url):
    yazi = ocr_client.get(image_url, as_array=True)
    logging.info(yazi)
    full = " ".join(yazi)
    matches = []
    matchnums = []
    truematch = None
    for yaziblok in yazi:
        try:
            wordbyword = yaziblok.split()
            if check_skippable_query(wordbyword, yaziblok):
                continue
            # çok ayrıntılı bir arama
            for advkelime in wordbyword:
                if advkelime[0].isdigit() and (advkelime.endswith("k") or advkelime.endswith(".")):
                    yaziblok = yaziblok.replace(advkelime, "")
            yaziblok = yaziblok.strip()
            if yaziblok.split()[0].isdigit():
                yaziblok = yaziblok.replace(yaziblok.split()[0], "")
            yaziblok = yaziblok.strip()
            logging.info("Filtered:"+yaziblok)
            search = client.subreddit("all").search(yaziblok)
            notmatched = False
            foundany = False
            for result in search:
                title = result.title
                directaccess = title == yaziblok
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
                print(
                    f"Found one!The name is {result.title} and the url is https://www.reddit.com{result.permalink}")
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
    return truematch
