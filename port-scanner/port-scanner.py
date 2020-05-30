#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import socket
import sys
import time
import Queue

#print_lock is used, when one thread is using a variable same
#time others cannot access it
print_lock = threading.Lock()

if len(sys.argv) != 2 :
    print('Please enter exactly one argument...')
    sys.exit(1)

host_ip = sys.argv[1]

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host_ip, port))
        with print_lock:
            print('Port: {} is open'.format(port))
        con.close()
    except:
        pass

def threader_func():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

q = Queue.Queue()

for x in range(100):
    t = threading.Thread(target=threader_func)
    t.daemon = True
    t.start()

for worker in range(1, 1024):
    q.put(worker)

q.join()
