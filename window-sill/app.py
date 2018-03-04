#!/usr/bin/env python
"""
Window Sill

Like py on a window sill.
"""
import argparse

from gui.tk_gui import TinkerGUI


# Constants
DESCRIPTION = """\
WINDOW SILL

A simple Python desktop application for Ubuntu and Mac.
"""


# Set command-line arguments
parser = argparse.ArgumentParser(description=DESCRIPTION,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--tba', action='store_true', help='To be announced.',)
parser.add_argument('command', nargs='?', default='null', help='Choose a command.')


#
# Main Block
#
def main():
    args = parser.parse_args()
    app = TinkerGUI()
    app.loop()


#
# Main Block
#
if __name__ == "__main__":
    main()
