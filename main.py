from threading import Thread

from bot import Bot
from client import client
import logging

def main():
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s]:%(message)s', level=logging.DEBUG, datefmt='%I.%M.%S')

    if client.read_only:
        logging.error('Hesap bilgileri doğru girilmedi veya bot read-only.')
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    bot_thread: Thread = Thread(target=Bot, args=(client,))
    bot_thread.start()
    # for sub in listeningbynew:
    #    threading.Thread(target=BotListenByNewThread, args=(sub,)).start()'
    logging.info('Bot thread started working')
    pass


if __name__ == '__main__':
    main()
