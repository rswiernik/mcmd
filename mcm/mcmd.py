# File: src/mcmd.py
# Description:
#   This file contains the source for the (M)ine(c)raft (M)anagement (D)aemon

import os
import sys
import socket
import time
import argparse
import logging
import grp


class mcm_server:
    def __init__(self, name="mc_server"):
        # this is a placeholder

    def start(self):
        # java -Xms1024M -Xmx3072M -jar minecraft_server.1.10.2.jar nogui
        SERVER_START_COMMAND="java -Xms1024M -Xmx3072M -jar minecraft_server.1.10.2.jar nogui"

def main(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
    args = parser.parse_args()

    LOG_FORMAT = '%(asctime)-15s %(message)s'
    LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
    LOG_LVL = logging.INFO

    if args.verbose:
        LOG_LVL = logging.DEBUG
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
    logging.debug('Verbose output enabled')

    SERVER_ADDRESS = "/tmp/mcmd_socket"

    logging.debug("Starting mcmd on port: {0}".format(SERVER_ADDRESS))



    logging.debug("Stopping mcmd")
    exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
