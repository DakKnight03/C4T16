import pyglet
import datetime
import time


# hour = now.minute
while True:
    now = str(datetime.datetime.now().time())
    if now >= "12:00:00.000000":
        music = pyglet.resource.media('tokyo_ghoul.mp3')
        music.play()

        pyglet.app.run()
