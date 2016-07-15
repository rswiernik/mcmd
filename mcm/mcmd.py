# File: src/mcmd.py
# Author: rswiernik
# Description:
#   This file contains the source for the (M)ine(c)raft (M)anagement (D)aemon

import argparse
import grp
import logging
import os
import socket
import sys
import time

from subprocess import call as run_cmd

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

class mcm_server:
    def __init__(self, name="mc_server"):
        self.server_location = "/tmp/minecraft_servers"
        self.name = name
        self.properties = {
            'server-port': '25566',
            'motd': 'For the greater good!',
            'level-seed': ''
        }
        logging.debug('Creating server w/ name: {0}'.format(self.name))

    def start(self, min_mem='1024M', max_mem='3072M', version='1.10.2'):
        """
        Start the minecraft server. This uses the python call function to shell
        out and actually call the server.

        Example (using method defaults):
          java -Xms1024M -Xmx3072M -jar minecraft_server.1.10.2.jar nogui
        """
        java_path = '/usr/bin/java'
        path = '/home/reed/Github/mcmd/_minecraft_files/_1server'
        server_start_cmd = '{0} -Xms{1} -Xmx{2} -jar {3}/minecraft_server.{4}.jar nogui > {5}/log.out &'
        server_start_cmd = server_start_cmd.format(java_path, min_mem, max_mem, path, version, path)
        logging.debug("Running server command:")
        logging.debug("> {0}".format(server_start_cmd))
        try:
            with cd(path):
                run_cmd([server_start_cmd], shell=True)
        except Exception as e:
            logging.warn('Error running server start command: {0}'.format(str(e)))

def main(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
    args = parser.parse_args()

    LOG_FORMAT = '[%(asctime)-20s %(levelname)-5s %(funcName)-12s] %(message)s'
    LOG_DATE = '%Y/%m/%d %H:%M:%S'
    LOG_LVL = logging.INFO

    if args.verbose:
        LOG_LVL = logging.DEBUG
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)

    logging.debug('Verbose output enabled')
    logging.info("Starting mcmd")

    this = mcm_server('server1')
    this.start()

    logging.info("Stopping mcmd")
    exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
