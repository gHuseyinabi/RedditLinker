import logging
import client
import re
from util.findpost import find_post
import praw.models
titlere = re.compile(
    r'(\d[0-9]? (hours|days|minutes|minute|day|hour|month|year|years|months) ago)|(\d[0-9]?(h|m|y))'
)

buttonwords = [
    'Vote',
    'Reply',
    'Share',
    'Report',
    'Save',
    'Give award'
]


def check_not_comment_body(query):
    logging.info(query)
    if titlere.search(query):
        if titlere.search(' '.join(query.split()[1:]).strip()):
            return query.split()[0]  # author
        return True

    return sum(buttonword in query for buttonword in buttonwords) > len(query.split()) / 2


def find_comment(uri=None, prepText=None):
    if not prepText:
        prepText = client.ocr_client.get(uri, True)
    print(prepText)
    author = None
    match = None
    found = False
    for query in prepText:
        check = check_not_comment_body(query)
        if isinstance(check, str):
            author = check
            logging.info(f'Author,{author}')
            continue
        elif check:
            print(query)
            continue
        if author is None:
            continue
        for comment_ in client.client.redditor(author).comments.new(limit=None):
            if query in comment_.body:
                match = comment_
                found = True
                break
        if found:
            break
    return match


def RedditLinkerGlobalFinder(img):
    imgPrep = client.ocr_client.get(img, True)
    if any('Posted by' in imgPrepText for imgPrepText in imgPrep):
        post = find_post(img)
        logging.info("Requested image was a submission.")
        return post
    else:
        comment = find_comment(prepText=imgPrep)
        return comment
    pass


__all__ = ['RedditLinkerGlobalFinder']
