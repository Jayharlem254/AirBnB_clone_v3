#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py) that
deletes out-of-date archives, using the function do_clean."""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = 'ubuntu'
env.key_filename = ['my_ssh_private_key']


def do_clean(number=0):
    """Deletes all out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number + 1))
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number + 1))

