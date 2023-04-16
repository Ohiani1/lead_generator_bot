import praw

reddit = praw.Reddit(
    client_id="goCW4r2J6JdPhiQDLdS5zg",
    client_secret="JIPIj30b3RuWNBVekK5aXJz-IKKCWg",
    user_agent="reddit bot",
    username="Alternative_Metal_89",
    password="Junior1235",
)

import random
import time

subreddit = reddit.subreddit("FreeKarma4You+FreeKarma4All+FreeKarma4U")
messages = ["upvoted, upvote in return?", "Great post, care to share the upvotes!"]

def karma():
  try:
    for submission in subreddit.stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(30)
  except:
    time.sleep(300)
    karma()
