#!/usr/bin/env python3
__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    Command line tool for obtaining keyboard ASCII codes
'''

# Import cli from parent directory.
# There's probably a better way to do this
import sys, os
sys.path.insert(0, os.path.abspath('..'))
from cli import cli, cli_controls

print("Use ctrl+c or ctrl+d to quit")
print(cli_controls.HIDE_CURSOR, end='\r')
while(1):
    # Get keypress
    key = cli.get_key()
    print(cli_controls.CLR_LINE + '\\x' + '\\x'.join(c.encode("ascii").hex() for c in key), end ='\r')

    # ctrl+c or ctrl+d
    if(key == '\x03' or key == '\x04'):
        print(cli_controls.SHOW_CURSOR, end='\r')
        exit()
