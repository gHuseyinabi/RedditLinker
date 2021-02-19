import praw.models
from typing import Final
formatted_link : Final = '[{}]({})'
found : Final = 'Bunu bulabildim:'
foundmuch : Final = 'Bunları bulabildim:'
notfound : Final = 'Bir şey bulamadım :('
resimyok : Final = 'Bir şey bulamadım çünkü bu postta resim yok.'
sourcecode : Final = '\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)'

replies : Final = {
    'commentauthor': {
        'tr': 'Yorumu yapan kişinin adı gözükmüyor ve yorumu yapanın adı olmadan yorumları bulamam.\r\nBelki bilerek '
              'gizlenmiştir? ',
        'other': 'Seems like image doesnt show the author\'s name. Maybe OP did it on purpose?'
    },
    'found': {
        'tr': 'Bunu bulabildim:',
        'other': 'I found this:'
    },
    'foundmuch': {
        'tr': 'Bunları bulabildim:',
        'other': 'I found these:'
    },
    'notfound': {
        'tr': 'Bir şey bulamadım.Belki silinmiştir?',
        'other': 'I did not found anything related to this post,maybe its deleted?'
    },
    'sourcecode': {
        'tr': '\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)',
        'other': '\r\n^[source code](https://github.com/gHuseyinabi/RedditLinker)'
    },
    'good': {
        'tr': 'tşk',
        'other': 'thx'
    },
    'bad': {
        'tr': ' peki',
        'other': ':('
    }
}


def getTranslatedReplyByName(key: str, subredditname: str) -> str:
    base = replies[key]
    if subredditname in tcsubredditleri:
        reply = base["tr"]
    else:
        reply = base["other"]
    return reply


tcsubredditleri : Final = ["kgbtr", "testyapiyorum", "svihs", "turkeyjerkey", "turkey", "svihstard", "mal"]  # <3


def get_proper_reply(posts, subredditname) -> str:
    formations = '\n'.join(list(
        formatted_link.format(post.title if isinstance(post, praw.models.Submission) else "Yoruma git", post.permalink)
        for post in posts))
    if posts:
        reply = replies["foundmuch"]
    else:
        reply = replies["notfound"]
    if subredditname in tcsubredditleri:
        reply = reply["tr"]
    else:
        reply = reply["other"]
    return reply + formations + getTranslatedReplyByName("sourcecode", subredditname)
