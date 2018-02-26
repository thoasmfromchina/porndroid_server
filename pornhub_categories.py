#!/usr/bin/env python
# -*- coding:utf-8 -*-
from libs.pornhub_categories_op import pornhub_categories_op
from time import sleep
import os, sys
from daemonize import Daemonize

#pid_folder = "/var/run/pornhub_categories"
#pid = "/var/run/pornhub_categories/pornhub_categories.pid"
pid = "/tmp/pid"

def main():
    #if os.path.exists(pid_folder) is True:
    #    pass
    #else:
    #    os.system("mkdir -p /var/run/pornhub_categories")
    while True:
        pornhub_categories_op()
        sleep(7200)


daemon = Daemonize(app="PornHub Categories", pid=pid, action=main)
daemon.start()
daemon.get_pid()
daemon.is_running()