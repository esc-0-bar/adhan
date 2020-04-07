#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Adhan Script"""

import requests
import constants
from datetime import datetime

r = requests.get(constants.url)
j = r.json()

fajr_time = j['data']['timings']['Fajr']
dhuhr_time = j['data']['timings']['Dhuhr']
asr_time = j['data']['timings']['Asr']
maghrib_time = j['data']['timings']['Maghrib']
isha_time = j['data']['timings']['Isha']

times = [fajr_time,dhuhr_time,asr_time,maghrib_time,isha_time]

def getPrayerTime():
    global times
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == '00:00':
        r = requests.get(constants.url)
        j = r.json()
        fajr_time = j['data']['timings']['Fajr']
        dhuhr_time = j['data']['timings']['Dhuhr']
        asr_time = j['data']['timings']['Asr']
        maghrib_time = j['data']['timings']['Maghrib']
        isha_time = j['data']['timings']['Isha']
        times = [fajr_time,dhuhr_time,asr_time,maghrib_time,isha_time]
    return times