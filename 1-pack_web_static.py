#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    script that generates a .tgz archive from the
    contents of the web_static folder
    Returns:
        archive path if the archive has been correctly generated.
    """
    filename = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        # create versions folder
        local("mkdir -p versions")

        # compress web_static folderr into the archive
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
