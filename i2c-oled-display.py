#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib3
import json
import bakebit_128_32_oled as oled


http = urllib3.PoolManager()
response = http.request('GET', 'http://127.0.0.1:9999/api/info')
# {"blowout":false,"blowout_weight":100,"current_weight":1,"increment":1}
status_dict = json.loads(response.data.decode('UTF-8'))

oled.init()  #initialze SEEED OLED display
oled.clearDisplay()          #clear the screen and set start position to top left corner
oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
oled.setPageMode()           #Set addressing mode to Page Mode

# Seems the 128x32 only have 4 rows.

oled.setTextXY(0,0)
oled.putString("Blowout: {}".format(status_dict['blowout']))
oled.setTextXY(0,1)
oled.putString("Current: {}".format(status_dict['current_weight']))
oled.setTextXY(0,2)
oled.putString("Max: {}".format(status_dict['blowout_weight']))
oled.setTextXY(0,3)
oled.putString("Increment: {}".format(status_dict['increment']))
