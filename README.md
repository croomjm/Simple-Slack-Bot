# Simple-Slack-Bot
This is a basic slack bot written in python inspired by a [version I found written in Ruby](https://github.com/kciter/simple-slack-bot). I wrote it to respond to all the happy birthday well-wishes from my coworkers in our various slack channels with a fun picture from one of our company events. In general, the text string to respond to and the response can easily be modified to perform other more complex behaviors.

The script ran continuously on Heroku and requires only the slack client library (see requirements.txt) and the slack channel token stored on the server as an environment variable.
