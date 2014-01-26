#!/usr/bin/python

import os, PIL

from PIL import Image

ios = (16, 29, 36, 40, 48, 50, 57, 58, 72, 76, 80, 96, 100, 114, 120, 128, 144, 152, 500, 512, 1024)
android = (12, 16, 24, 32, 36, 48, 57, 72, 96, 114, 128, 144, 500, 512, 1024)
windows = (16, 32, 22, 44, 64)
blackberry = (44, 63, 68, 92)
chrome = (16, 48, 128)

PLATFORMS = ["iOS", "Android", "Windows", "Blackberry", "Chrome"]

DEFAULT_ICON_FILE = "default.png"

for platform in PLATFORMS:
    _platform = platform.lower()
    logo = None
    try:
        logo = Image.open("%s.png" % _platform)
    except:
        pass
    try:
        logo = Image.open(DEFAULT_ICON_FILE)
    except:
        pass

    if logo:
        if not os.path.exists(platform):
            os.makedirs(platform)
        for size in globals()[_platform]:
            _logo = logo.copy().resize((size, size), Image.ANTIALIAS)
            _logo.save("%s/%sx%s.png" % (_platform, size, size))
            del _logo
        print "%s's Done." % platform