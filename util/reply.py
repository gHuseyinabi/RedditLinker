formatted_link = '[{}]({})'

replies  = {
    'found': {
        'tr': 'Bunu bulabildim:',
        'other': 'I found this:'
    },
    'notfound': {
        'tr': 'Bir şey bulamadım.Belki silinmiştir?',
        'other': 'I did not found anything related to this post,maybe its deleted?'
    },
    'sourcecode': {
        'tr': '\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)',
        'other': '\r\n^[source code](https://github.com/gHuseyinabi/RedditLinker)'
    }
}


def getTranslatedReplyByName(key, subredditname):
    base = replies[key]
    if subredditname in tcsubredditleri:
        reply = base['tr']
    else:
        reply = base['other']
    return reply


tcsubredditleri  = [
    'kgbtr',
    'testyapiyorum',
    'svihs',
    'turkeyjerkey',
    'turkey',
    'svihstard',
    'mal',
    'ateistturk'
]


def get_proper_reply(post, subredditname):
    if post:
        key = 'found'
        formations = formatted_link.format('Tıkla',post.permalink)
    else:
        key = 'notfound'
        formations = ""
    reply = getTranslatedReplyByName(key,subredditname)
    source = getTranslatedReplyByName('sourcecode', subredditname)
    return reply + formations + source
