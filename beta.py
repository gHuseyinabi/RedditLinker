import client
import re
import findpost
import praw.models
titlere = re.compile("(\d[0-9]? (hours|days|minutes|minute|day|hour|month|year|years|months) ago)|(\d[0-9]?(h|m|y))")

buttonwords = [
    "Vote",
    "Reply",
    "Share",
    "Report",
    "Save",
    "Give award"
]


def check_not_comment_body(query: str):
    print("|||||" + query + "|||||")
    if titlere.search(query):
        if titlere.search(" ".join(query.split()[1:]).strip()):
            return query.split()[0]  # author
        return True

    return sum(buttonword in query for buttonword in buttonwords) > len(query.split()) / 2


class CommentNotFoundException:
    error = "Comment Not Found"

    def __eq__(self, other):
        return self.error == other.error

    def __repr__(self):
        return self.error

    def __init__(self, err=None):
        if err:
            self.error = err

    pass


class CommentAuthorNotFoundException:
    error = "Comment Author Not Found"

    def __eq__(self, other):
        return self.error == other.error

    def __repr__(self):
        return self.error

    def __init__(self, err=None):
        if err:
            self.error = err

    pass


class UnsatisfiedFunctionParametersException:
    error = "Parameters Don't require the information that need to run the function."

    def __eq__(self, other):
        return self.error == other.error

    def __repr__(self):
        return self.error

    def __init__(self, err=None):
        if err:
            self.error = err

    pass


def find_comment(uri=None, prepText=None) -> praw:
    if not prepText and uri:
        raise UnsatisfiedFunctionParametersException()
    if not prepText:
        prepText = client.ocr_client.get(uri, True)
    print(prepText)
    author = None
    match = None
    found = False
    for query in prepText:
        check = check_not_comment_body(query)
        if isinstance(check, str):
            author = check
            print("Author,", author)
            continue
        elif check:
            print(query)
            continue
        if author is None:
            raise CommentAuthorNotFoundException()
        for comment_ in client.client.redditor(author).comments.new(limit=None):
            if query in comment_.body:
                match = comment_
                found = True
                break
        if found:
            break
    if not match:
        raise CommentNotFoundException()
    return match


def RedditLinkerGlobalFinder(img: str):
    imgPrep = client.ocr_client.get(img, True)
    if any("Posted by" in imgPrepText for imgPrepText in imgPrep):
        post = findpost.find_post(img)
        return post["matches"]
    else:
        try:
            comment = find_comment(prepText=imgPrep)
            return [comment]
        except:
            return []
    pass

