allicons
========

allicons is a lightweight tool, written in Python which will create iOS, Android, Windows, BlackBerry and Chrome's icons in few seconds.

Requirements
------------

allicons was built upon Python Image Library (PIL). To get allicons working you need to install PIL or Pillow (recommended). [Here is the full installation guide] [1]

[1]:http://pillow.readthedocs.org/en/latest/installation.html

Installation
------------

```
git clone https://github.com/talhashraf/allicons.git
cd allicons
chmod +x allicons.py
```

Usage
-----

Create default.png where allicons.py is located and run ```./allicons.py``` then you will have 5 platform icons in their respective directories **OR** you can also have platform specific icons by creating **[platform]**.png for each platform.

For example:

  - ios.png
  - android.png
  - blackberry.png
  - windows.png
  - chrome.png

*make sure there is no default.png while you go this way because default.png supersede this option*

Once you have platform specific icon files, run ```./allicons.py``` then you will have 5 platform icons in their respective directories.