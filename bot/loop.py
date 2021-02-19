import logging
from util import reply
from . import beta
import praw.models

def ExecuteCommand(comment: praw.models.Comment) -> None:
    logging.info("Le command arrived.")
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
            logging.debug(f"{final}\n\n")
    else:
        comment.reply(reply.resimyok)

__all__ = ['ExecuteCommand']