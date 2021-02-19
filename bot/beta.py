from typing import Union
import client
import re
from util.findpost import find_post
import praw.models
titlere = re.compile('(\d[0-9]? (hours|days|minutes|minute|day|hour|month|year|years|months) ago)|(\d[0-9]?(h|m|y))')

buttonwords = [
    'Vote',
    'Reply',
    'Share',
    'Report',
    'Save',
    'Give award'
]


def check_not_comment_body(query: str) -> bool:
    print('|||||' + query + '|||||')
    if titlere.search(query):
        if titlere.search(' '.join(query.split()[1:]).strip()):
            return query.split()[0]  # author
        return True

    return sum(buttonword in query for buttonword in buttonwords) > len(query.split()) / 2



def find_comment(uri=None, prepText=None) -> Union[praw.models.Comment,type[None]]:
    if not prepText and uri:
        raise Exception()
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
            print('Author,', author)
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
    if not match:
        return None
    return match


def RedditLinkerGlobalFinder(img: str) -> list:
    imgPrep = client.ocr_client.get(img, True)
    if any('Posted by' in imgPrepText for imgPrepText in imgPrep):
        post = find_post(img)
        return post['matches']
    else:
        try:
            comment = find_comment(prepText=imgPrep)
            return [comment]
        except:
            return []
    pass

__all__ = ['RedditLinkerGlobalFinder']