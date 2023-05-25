import praw

reddit = praw.Reddit(
    client_id="cKhT2o_mVkHnyHySPtMjsw",
    client_secret="buT_YxPSHuuKeU2RSVZ7_Xtau6QndQ",
    user_agent="bot",
    username="AdPrestigious8977",
    password="Adam2003@",
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
