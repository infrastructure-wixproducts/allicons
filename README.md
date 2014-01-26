allicons
========

allicons is a lightweight tool, written in Python which will create iOS, Android, Windows, BlackBerry and Chrome's icons in few seconds.
<hr />
###### Requirements
allicons was built upon [Python Image Library (PIL)](https://github.com/python-imaging/Pillow). To get allicons working you need to install PIL or Pillow (recommended). Here is the full installation guide: http://pillow.readthedocs.org/en/latest/installation.html
<br /><br />
###### Installation
```sh
git clone https://github.com/talhashraf/allicons.git
cd allicons
chmod +x allicons.py
```
<br />
###### Usage
Create default.png where allicons.py is located and run

    ./allicons.py
then you will have 5 platform icons in their respective directories
<br /><br />
OR you can also have platform specific icons by creating [platform].png for each platform. For example, ios.png, android.png, blackberry.png, windows.png and chrome.png (make sure there is no default.png while you go this way because default.png supersede this option). Once you have platform specific icon files, run

    ./allicons.py
then you will have 5 platform icons in their respective directories