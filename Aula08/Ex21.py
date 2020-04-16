from pygame import mixer

mixer.init()
mixer.music.load('Sweden.mp3')

mixer.music.play()

import time

time.sleep(360)