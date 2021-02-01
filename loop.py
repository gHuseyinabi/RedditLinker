from client import client, client_info
from findpost import find_post
import reply

def loop(subredditname):
    print("Başlıyor...")
    print("Listening comments at " + subredditname)
    stream = client.subreddit(subredditname).stream

    try:
        for comment in stream.comments(skip_existing=True):
            try:
                cbody = comment.body.lower()
                if "u/redditlinker" in cbody or "u/reddit_linker" in cbody:
                    print("Aha!Found a match.")
                    post = comment.submission
                    "    "
                    canlook = False
                    if hasattr(post, 'preview'):
                        canlook = True
                    if canlook:
                        Post = find_post(post.preview["images"][0]["source"]["url"])
                        if Post is None:
                            comment.reply(reply.notfound + reply.sourcecode)
                        else:
                            comment.reply(reply.found.format(Post.title, Post.permalink) + reply.sourcecode)
                            print("[UYARI] Replied",reply.found.format(Post.title, Post.permalink))
                    else:
                        comment.reply(reply.resimyok)
            except Exception as e:
                print(e)
                continue
    except:
        loop(subredditname)
