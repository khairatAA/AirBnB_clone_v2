#!/usr/bin/python3
"""2-do_deploy_web_static module"""
import os
from datetime import datetime
from fabric.api import local, run, env, put

env.hosts = ["54.86.45.44", "52.91.122.202"]
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """Distributes an archive to your web servers,
    using the function do_deploy
    Args:
        archive_path:
    """

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_without_ext = os.path.splitext(os.path.basename(
            archive_path))[0]

        file_dir = "/data/web_static/releases/{}".format(
                file_without_ext)

        uncompressed_dir = "{}/".format(file_dir)

        run("mkdir -p {}".format(file_dir))

        run(
                "tar -xvf /tmp/{} -C {}".format(
                    os.path.basename(archive_path),
                    uncompressed_dir
                    )
                )

        run("rm -f /tmp/{}".format(
            os.path.basename(archive_path)))

        run("rm -rf {}".format("/data/web_static/current"))

        run("ln -s {} {}".format(
            file_dir, "/data/web_static/current"))

        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
