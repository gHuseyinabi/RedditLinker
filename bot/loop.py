import praw

from client.client import client
from util.findpost import find_post
from util import reply
from . import beta
import praw.models
from util.log import log


def ExecuteCommand(comment):
    log("Replying")
    print("Aha!Found a match.")
    post = comment.submission
    canlook: bool = hasattr(post, 'preview')
    if canlook:
        Post = beta.RedditLinkerGlobalFinder(post.preview["images"][0]["source"]["url"])
        subreddit = comment.subreddit.display_name.lower()
        l = 1
        try:
            l = Post.get("matches")
        except:
            pass
        if Post is None or l is None:
            comment.reply(reply.get_proper_reply([Post],subreddit))
        else:
            if hasattr(Post,"get"):
                posts = Post.get("matches")
            else:
                posts = Post
            final = reply.get_proper_reply(posts, subreddit)
            print("[Yanit verildi]", final)
            comment.reply(final)
            log(f"{final}\n\n")
    else:
        comment.reply(reply.resimyok)

__all__ = ['ExecuteCommand']
"""def loop(subredditname: str) -> None:
    print("Başlıyor...")
    
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
        loop(subredditname)"""
