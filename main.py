from client import client
import loop
import time
import config
from praw.models import Comment
def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    #loop.loop("test")
    print("listening globally")
    while True:
        print("another loop")
        for item in client.inbox.unread(limit=None):
            try:
                print("found one")
                if not isinstance(item, Comment):
                    continue
                print("passed")
                lower = item.body.lower()
                if lower == "u/reddit_linker":
                    print("aha")
                    loop.ExecuteCommand(item)
                else:
                    print("nope",lower)
            except Exception as e:
                print(f"Oops,thats stinky!Error:{e}")
            item.mark_read()
        time.sleep(15)
    pass


if __name__ == '__main__':
    main()
