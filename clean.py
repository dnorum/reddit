#! /usr/bin/python3

# Import stuff
import praw
import pandas as pd
import datetime as dt
import time
from datetime import date

# Create human-readable timestamp conversion
def get_date(created):
    return dt.datetime.fromtimestamp(created)

# Set up Reddit credentials - should be put into external file...:
# [CLIENT ID]
# [CLIENT SECRET]
# [USERNAME]
# [PASSWORD]
reddit = praw.Reddit(client_id='[CLIENT ID]', \
                     client_secret='[CLIENT SECRET]', \
                     user_agent='clean', \
                     username='[USERNAME]', \
                     password='[PASSWORD]')

# Set up my account for scraping
redditor = reddit.redditor("[USERNAME]")

# Set up data structure
comments_dict = {	"body":[], \
			"created_utc":[], \
			"distinguished":[], \
			"edited":[], \
			"id": [], \
			"permalink": [], \
			"score":[]	}

# Scan over all of my comments
for comment in redditor.comments.new():

	# Wait a skoche so I don't get 429ed
	time.sleep(15)

	# Store the pertinent details
	comments_dict["body"].append(comment.body)
	comments_dict["created_utc"].append(comment.created_utc)
	comments_dict["distinguished"].append(comment.distinguished)
	comments_dict["edited"].append(comment.edited)
	comments_dict["id"].append(comment.id)
	comments_dict["permalink"].append(comment.permalink)
	comments_dict["score"].append(comment.score)

	# Blank out comment body
	comment.edit(".")

	# Wait a skoche so I don't get 429ed
	time.sleep(15)

	# Nuke 'em.
	comment.delete()

	# Wait a skoche so I don't get 429ed
	time.sleep(15)

# Turn the stored comments into a data frame
comments_data = pd.DataFrame(comments_dict)

# Add human-readable timestamp
_timestamp = comments_data["created_utc"].apply(get_date)
comments_data = comments_data.assign(timestamp = _timestamp)

# Output my comments
filename = str(date.today()) + '_' + dt.datetime.now().strftime('%H-%M-%S') + '.csv'
comments_data.to_csv(filename, index=False)
