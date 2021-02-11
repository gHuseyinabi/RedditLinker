import loop
from log import log
from ocrclient import OCR
from praw.models import Comment
from praw import Reddit
import time
import threading


def Bot(client: Reddit):
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
