import loop
from log import log
from client import client, ocr_client
from praw.models import Comment
import time
import threading

# listeningbynew = ["kgbtr", "svihs", "turkeyjerkey", "ateistturk", "turkey", "burdurland"]

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
                    threading.Thread(target=loop.ExecuteCommand, args=(item,)).start()
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

if False:
    """
def BotListenByNewThread(subreddit):
    print("Listening by " + subreddit + " new")
    substream = client.subreddit(subreddit).stream
    for post in substream.submissions(skip_existing=True):
        canlook: bool = False
        if hasattr(post, 'preview'):
            canlook = True
        if canlook:
            imgurl = post.preview["images"][0]["source"]["url"]
            ocr = ocr_client.get(imgurl)
            print("IS_REDDIT_POST" + "posted by" in ocr.lower())
            print(ocr)
        print(post.title)
        print(post.subreddit.display_name)
        print(canlook)

        pass"""