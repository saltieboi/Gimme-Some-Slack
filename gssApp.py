import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
SLACK_BOT_TOKEN = 'xoxb-4900349419124-4894967171973-mKAjffuiMaI3zw5xOz0HPX42'
SLACK_SIGNING_SECRET = '958ab322ca55a8ed39c700fa65e291f4'
# SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
# SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)


# Add functionality here
@app.event("app_home_opened")
def opened(say):
    say("I'm alive")


@app.message("test")
def reply_to_test(say):
    say("Yes, tests are important!")


@app.message("message")
def reply_to_test(say):
    say("Got your message")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
