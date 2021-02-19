from . import loop
from praw.models import Comment
from praw import Reddit
import time
import threading
import logging


def Bot(client: Reddit) -> None:
    logging.info(f'Started working')
    while True:
        for item in client.inbox.unread(limit=None):
            try:
                logging.info(f'[INFO]Got comment at {time.time()}')
                if not isinstance(item, Comment):
                    continue
                lower = item.body.lower()
                if 'u/reddit_linker' in lower:
                    logging.info('New work')
                    threading.Thread(target=loop.ExecuteCommand, args=(item,)).start()
                elif lower == 'good bot':
                    logging.info('Good bot')
                    item.reply('ヽ(•‿•)ノ')
                elif lower == 'bad bot':
                    logging.info('Bad bot')
                    item.reply('( ._.)')
                else:
                    print('nope', lower)
            except Exception as e:
                logging.error(e)
            item.mark_read()
        time.sleep(30)

__all__ = ['Bot']