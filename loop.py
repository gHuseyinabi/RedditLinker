from client import client
from findpost import find_post
import reply


def loop(subredditname) -> None:
    print("Başlıyor...")
    print("Listening comments at " + subredditname)
    stream = client.subreddit(subredditname).stream

    try:
        for comment in stream.comments(skip_existing=True):
            try:
                cbody: str = comment.body.lower()
                if "u/redditlinker" in cbody or "u/reddit_linker" in cbody:
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
                            if len(Post.get("matches")) == 1:
                                _Post = post.get("match")
                                comment.reply(reply.found.format(_Post.title, _Post.permalink) + reply.sourcecode)
                                print("[UYARI] Replied", reply.found.format(_Post.title, _Post.permalink))
                            else:
                                posts = Post.get("matches")
                                formattedposts = '\n'.join(
                                    list(reply.formatted_link.format(post.title, post.permalink) for post in posts))
                                print(reply.foundmuch + formattedposts)
                    else:
                        comment.reply(reply.resimyok)
            except Exception as e:
                print(e)
                continue
    except Exception as e:
        print("[error]", e)
        loop(subredditname)
