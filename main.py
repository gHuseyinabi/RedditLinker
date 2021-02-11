from threading import Thread

from bot import *
from client import client
from findpost import find_post


def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    bot_thread: Thread = threading.Thread(target=Bot, args=(client,))
    bot_thread.start()
    # for sub in listeningbynew:
    #    threading.Thread(target=BotListenByNewThread, args=(sub,)).start()"
    print("Bot thread started working")
    pass


if __name__ == '__main__':
    main()
