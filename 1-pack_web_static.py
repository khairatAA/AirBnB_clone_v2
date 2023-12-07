#!/usr/bin/python3
"""1-pack_web_static module"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Fabric script that generates a .tgz archive
    from the contents of the web_static folder of
    your AirBnB Clone repo
    """

    """Check if version dir exits:"""
    path = "versions"
    if not os.path.exists(path):
        os.makedirs(path)

    """Get the current time and date"""
    currentDateAndTime = datetime.now()
    archiveTime = currentDateAndTime.strftime("%Y%m%d%H%M%S")

    """Naming of the archive file"""
    name_of_archive = "web_static_{}.tgz".format(archiveTime)

    archive_path = "{}/{}".format(path, name_of_archive)

    content = "web_static"

    """Using of the tar command"""
    result = local("tar -cvzf {} {}".format(archive_path, content))

    if result.succeeded:
        return archive_path

    return None
