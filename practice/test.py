# -*- coding: utf-8 -*-
# UI自动化

import uiautomator2 as u2
import os
import time

os.system('start ')
# os.system('start cmd.exe&&python -m weditor')
d = u2.connect()

d.xpath('//*[@resource-id="com.beantechs.launcher:id/gv"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
d(resourceId="com.beantechs.settings:id/customItem").click()
d(resourceId="com.beantechs.settings:id/back").click()
d(resourceId="com.android.systemui:id/applist_btn").click()
