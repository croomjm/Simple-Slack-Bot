#!/usr/bin/env python

import time,os
from slackclient import SlackClient

BOT_NAME = 'bday_bot'
match_pattern = "happy.*b.*day"
image = "http://imgur.com/a/ddeFW"

sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def regex_test(w):
	import re
	pattern = re.compile(match_pattern, re.I)
	return bool(re.search(pattern, w))

if __name__ == "__main__":
	if sc.rtm_connect():
		while True:
			new_evts = sc.rtm_read()
			if new_evts:
				for evt in new_evts:
					if "type" in evt:
						if evt["type"] == "message" and "text" in evt:
							channel = evt["channel"]
							if regex_test(evt["text"]):
								sc.api_call(
									"chat.postMessage",
									as_user = "true",
									channel = channel,
									text = "Huzzah!\n" + image,
									)
