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
from playsound import playsound


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    for t in gpt.getPrayerTime():
        time.sleep(.5)
        if current_time == t:
            playsound(constants.sound)
        