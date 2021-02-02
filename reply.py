formatted_link = '[{}]({})'
found = 'Bunu bulabildim:'
foundmuch = 'Bunları bulabildim:'
notfound = 'Bir şey bulamadım :('
resimyok = 'Bir şey bulamadım çünkü bu postta resim yok.'
sourcecode = '\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)'

replies = {
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
        'tr':'\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)',
        'other':'\r\n^[source code](https://github.com/gHuseyinabi/RedditLinker)'
    },
    'good':{
        'tr':'tşk',
        'other':'thx'
    },
    'bad':{
        'tr':' peki',
        'other': ':('
    }
}

def getTranslatedReplyByName(key: str,subredditname: str) -> str:
    base = replies[key]
    if subredditname in tcsubredditleri:
        reply = base["tr"]
    else:
        reply = base["other"]
    return reply


tcsubredditleri = ["kgbtr","testyapiyorum","svihs","turkeyjerkey","turkey"]



def get_proper_reply(posts,subredditname) -> str:
    formations = '\n'.join(list(formatted_link.format(post.title, post.permalink) for post in posts))
    reply = replies["foundmuch"]
    if subredditname in tcsubredditleri:
        reply = reply["tr"]
    else:
        reply = reply["other"]
    return reply + formations + getTranslatedReplyByName("sourcecode",subredditname)
