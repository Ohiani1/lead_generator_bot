import praw

reddit = praw.Reddit(
    client_id="kyqQ6JP2lxvMS74AGt4Sqg",
    client_secret="0oOqkyTzSn-9g3A7En-CsSls_dN01g",
    user_agent="reddit bot",
    username="Emotional_Shirt_7654",
    password="Junior1235",
)

import random
import time

subreddit = reddit.subreddit("FreeKarma4All+FreeKarma4U")
messages = ["upvoted, upvote in return?", "Great post, care to share the upvotes!"]

def karma():
  try:
    for submission in subreddit.stream.submissions():
      submission.upvote()
      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])
      time.sleep(40)
  except:
    time.sleep(300)
    karma()
    
karma()
