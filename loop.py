from client import client
from findpost import find_post
import reply
from config import config
import time

def loop(subredditname: str) -> None:
    print("Başlıyor...")
    log_stream = open(config.get("logFile") if "logFile" in config else "default.log","w")
    print("Listening comments at " + subredditname)
    stream = client.subreddit(subredditname).stream

    try:
        for comment in stream.comments(skip_existing=True):
            try:
                cbody: str = comment.body.lower()
                if "u/redditlinker" in cbody or "u/reddit_linker" in cbody:
                    log_stream.write("Replying")
                    print("Aha!Found a match.")
                    post = comment.submission
                    canlook: bool = False
                    if hasattr(post, 'preview'):
                        canlook = True
                    if canlook:
                        Post = find_post(post.preview["images"][0]["source"]["url"])
                        if Post is None or Post.get("match") is None:
                            comment.reply(reply.notfound + reply.sourcecode)
                        else:
                            posts = Post.get("matches")
                            final = reply.get_proper_reply(posts)
                            print("[Yanit verildi]", final)
                            comment.reply(final)
                    else:
                        comment.reply(reply.resimyok)
            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print("[error]", e)
        loop(subredditname)
