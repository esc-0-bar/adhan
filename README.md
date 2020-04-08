
# Adhan

A python script to start adhan when it is time for prayer for muslims.

  - Install all the requirments
  - Run the script
  - Make it a startup program
  - BOOM!!!

### Change Location or Sound

Default Location is Dhaka, Bangladesh.

Change Location -
- Open ```constants.py``` in any text editor.
- Change the city and country as your need.
- Save it

There is a default adhan sound named ```adhan.mp3``` in assets folder.

Change Sound -
- Open assets folder and replace the sound with your sound
- Open ```constants.py``` in any text editor.
- Change sound with your new sound name.
- Save it

NOTE : The sound must be .mp3 or .wav format.

### Tech

Adhan uses a number of open source projects to work properly:

* [Python3] - High-level programming language!
* [VSCode] - awesome text editor
* [playsound] - Pure Python, cross platform, single function module with no dependencies for playing sounds.
* [Requests] - Python HTTP for Humans


And of course Adhan itself is open source with a public repository on GitHub.

### Installation

Adhan requires [Python](https://python.org/) v3 to run.

Install the dependencies to run the script.

```sh
$ git clone https://github.com/i-am-ahad/adhan
$ cd adhan
$ cp * ~/my-startups-scripts/adhan
$ cd ~/my-startups-scripts/adhan
$ pip3 install -r requirments.txt
$ python3 __init__.py
```

### Make this a startup program
```sh
$ sudo mv adhan.conf /etc/init 
```
Manual starting/stopping is done with ```sudo service mystartupscript start``` and ```sudo service mystartupscript stop```


### Issues
If you find any problem, please create an issue in the Issues section. So, that it can fix fast.


### Python Package Index (PIP)

Adhan requires the following packages. Instructions on how to use them in your own application are linked below.

| Package | Documentation |
| ------ | ------ |
| playsound | [https://pypi.org/project/playsound][play-sound] |
| requests | [https://pypi.org/project/requests][r-equests] |



### Development

Want to contribute? Great! :heart:

Make a change in your file, run ```python3 __init__.py``` and instantaneously see your updates!

### Todos

 - Make a function to stop playing the audio file
 - Create threads to make it more interactive
 - Make a GUI

License
----

Apache License 2.0

![](assets/LICENSE.png)


**Free Software, Hell Yeah!**

   [play-sound]: <https://pypi.org/project/playsound/>
   [r-equests]: <https://pypi.org/project/requests>
