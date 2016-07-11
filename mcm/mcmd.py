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


LOG_FORMAT = '%(asctime)-15s %(message)s'
LOG_DATE = '%m/%d/%Y %H:%M:%S %Z  '
LOG_LVL = logging.INFO


def main(args):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', help='enable verbose output', action='store_true')
    #parser.add_argument('-k', '--keyboard', action='store', dest='kbl_file',
    #    type=str, help='The file path to the kbl file you would like to use.')
    #parser.add_argument('-o', '--output-file', action='store', dest='outputFilename',
    #    type=str, default='output.layout', help='Layout output filename')
    #parser.add_argument('-f', '--firmware', action='store', dest='firmwareName',
    #    type=str, default='tmk', help='Fireware layout style to output to file')
    args = parser.parse_args()

    if args.verbose:
        LOG_LVL = logging.DEBUG
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE, level=LOG_LVL)
    logging.debug('Verbose output enabled')

    logging.debug("Starting mcmd - {}".format(""))


    logging.debug("Stopping - {}".format(""))
    exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
