import webbrowser
import time
import random

websites = random.choice([
    "youtube.com",
    "repl.it",
    "codesandbox.com",
    "codepen.io",
    "github.com",
    "instagram.com",
    "netflix.com",
    "duckduckgo.com",
    "microsoft.com",
    "developer.android.com",
    "myactivity.google.com",
    "developer.apple.com",
    "xbox.com",
    "spotify.com",
    "dropbox.com",
    "uber.com",
	  "google.com",
    "pinterest.com",
    "instacart.com",
    "reddit.com",
    "lyft.com",
])

formatted = "https://{}".format(websites)

while True:
    webbrowser.open(formatted)
    time.sleep(3)
