from client import client
import loop
import time
from praw.models import Comment,Submission
from log import log
import threading

listeningbynew = ["kgbtr","svihs","turkeyjerkey","ateistturk","turkey"]
def Bot():
    log(f"[BOT]Started working at {time.time()}")
    print("in function Bot()")
    while True:
        print("Loop")
        for item in client.inbox.unread(limit=None):
            try:
                log(f"[INFO]Got comment at {time.time()}")
                if not isinstance(item, Comment):
                    continue
                print("passed")
                lower = item.body.lower()
                if "u/reddit_linker" in lower:
                    print("aha")
                    threading.Thread(target=loop.ExecuteCommand, args=(item)).start()
                elif lower == "good bot":
                    item.reply("ヽ(•‿•)ノ")
                elif lower == "bad bot":
                    item.reply("( ._.)")
                else:
                    print("nope", lower)
            except Exception as e:
                print(f"Oops,thats stinky!Error:{e}")
                log(f"[ERROR]:{e}\n")
            item.mark_read()
        time.sleep(15)


def BotListenByNewThread(subreddit):
    log("Listening by new thread working")
    print("Listening by new thread working")
    substream = client.subreddit(subreddit).stream
    while True:
        for post in substream.submissions(skip_existing=True):
            canlook: bool = False
            if hasattr(post, 'preview'):
                canlook = True
            print(post.title)
            print(post.subreddit.display_name)
            print(canlook)
        pass


def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    # loop.loop("test")
    bot_thread = threading.Thread(target=Bot, args=())
    bot_thread.start()
    for sub in listeningbynew:
        threading.Thread(target=BotListenByNewThread, args=(sub,)).start()
    print("Bot thread started working")
    pass


if __name__ == '__main__':
    main()
