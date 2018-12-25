#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import subprocess

ADD_SEC = 3


t = int(time.time())
print('py_time:', t)

t = t + ADD_SEC

proc = subprocess.Popen(['./challenge'], env={ 'TIME': str(t), 'LD_PRELOAD': './libtime_env.so' }, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
datas = str(proc.communicate(b'dead')[0]).split()
key = int(datas[-1][:-3])
print('py_key:', key)
time.sleep(3)

proc2 = subprocess.Popen(['./challenge'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
recv = str(proc2.communicate(bytes(key))[0])
# proc2.communicate(str(key))
print(recv)



