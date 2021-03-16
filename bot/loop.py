import logging
from util import reply
from . import beta


def ExecuteCommand(comment):
    logging.info('Command arrived.')
    post = comment.submission
    subreddit = comment.subreddit.display_name.lower()
    canlook: bool = hasattr(post, 'preview')  # o => obj
    if canlook:
        Post = beta.RedditLinkerGlobalFinder(
            post.preview['images'][0]['source']['url'])
        if Post is None:
            comment.reply(reply.get_proper_reply(Post, subreddit))
        else:
            final = reply.get_proper_reply(Post, subreddit)
            comment.reply(final)
            logging.info(final)
    else:
        comment.reply(reply.getTranslatedReplyByName(
            'notfound', subredditname=subreddit))
