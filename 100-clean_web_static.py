#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.34.7', '35.153.226.247']


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
    """
    index = 1 if int(index) == 0 else int(index)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(index)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(index)]
        [run("rm -rf ./{}".format(a)) for a in archives]
