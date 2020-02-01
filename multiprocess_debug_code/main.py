#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is an example to use the multiprocess debug feature
# of vscode.
# Steps needed:
# 1) Open an integrated terminal into the active workspace, and run the main.py 
# file with command: 
# $> python main.py
# This will spawn a new process executing the execute.process_identifier() function.
# This function contains a breakpoint.
# Thus, upon giving the command, the execution will stop at the predefined breakpoint
# with the message "Waiting for debugger attach".
# 2) Make sure you have a proper debug configuration for the project.
# it should look like this:
# {
#     "name": "Python: Attach",
#     "type": "python",
#     "request": "attach",
#     "port" : 5678
# }
# After starting the main.py, go in the debug section of vscode, then in the upper dropdown list
# select the configuration "Python: Attach" you just set up.
# 3) Click play: the debugger should detect the waiting process, and you will see the breakpoint set.
# Note that any print output which is after the breakpoint will be shown in terminal window.

import execute
import os
from multiprocessing import Process


print("[MAIN] Starting.")
print("[MAIN] Creating subprocess..")

p = Process(target=execute.process_identifier)
p.start()

p.join()

print("[MAIN] Subprocess returned.")