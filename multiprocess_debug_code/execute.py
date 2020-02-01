#!/usr/bin/env python3
import os
import ptvsd


def process_identifier():

    # 5678 is the default attach port in the VS Code debug configurations
    print("Waiting for debugger attach")
    ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.wait_for_attach()
    breakpoint()

    print("Hello, this is the forked process")
    print("My pid is:", os.getpid())