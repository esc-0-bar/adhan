#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Adhan Script"""

sound = 'assets/azan.mp3'
city = 'Dhaka'
Country = 'Bangladesh'

url = 'https://api.aladhan.com/timingsByAddress?address=%s,%s'%(city,Country)