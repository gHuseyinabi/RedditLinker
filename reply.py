formatted_link = '[{}]({})'
found = 'Bunu bulabildim:'
foundmuch = 'Bunları bulabildim:'
notfound = 'Bir şey bulamadım :('
resimyok = 'Bir şey bulamadım çünkü bu postta resim yok.'
sourcecode = '\r\n^[kaynak kodum](https://github.com/gHuseyinabi/RedditLinker)'


def get_proper_reply(posts) -> str:
    formations = '\n'.join(list(formatted_link.format(post.title, post.permalink) for post in posts))
    return foundmuch + formations + sourcecode
