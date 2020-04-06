#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Adhan Script"""


import requests
import constants
import gpt
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print('Current time ',current_time)

    for t in gpt.getPrayerTime():
        time.sleep(.5)
        print(t)
        if current_time == t:
            play(AudioSegment.from_mp3(constants.song))
        