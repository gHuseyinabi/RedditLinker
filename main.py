from client import client
import findpost
import reply


def main():
    if client.read_only:
        raise Exception('Hesap bilgileri doğru girilmedi veya bot read-only.')
    SHOW_ONE_POST = False
    Posts = findpost.find_post("test.png")
    if Posts is None:
        raise Exception("didnt find any post")
    if SHOW_ONE_POST:
        print(Posts.get("match"))
    else:
        posts = Posts.get("matches")
        formattedposts = '\n'.join(list(reply.formatted_link.format(post.title, post.permalink) for post in posts))
        print(reply.foundmuch + formattedposts)
    pass


if __name__ == '__main__':
    main()
