#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import execute
import os
from multiprocessing import Process


print("[MAIN] Starting.")
print("[MAIN] Creating subprocess..")

p = Process(target=execute.process_identifier)
p.start()

p.join()

print("[MAIN] Subprocess returned.")