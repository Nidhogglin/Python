#!usr/bin/env python3
# coding: utf-8
# @time :2020/11/4 17:14

import threading
import asyncio


async def hello():
    print('Hello World! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()