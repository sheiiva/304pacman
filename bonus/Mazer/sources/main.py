#!/usr/bin/env python3
############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

from sys import argv

from sources.Usage import Usage
from sources.ArgumentManager import ArgumentManager
from sources.Mazer import Mazer


def main():

    argsManager = ArgumentManager()

    if argsManager.needHelp(argv):
        Usage()
    elif argsManager.checkArgs(argv) == 84:
        print()
        Usage()
        exit(84)
    else:
        Mazer(int(argv[1]), int(argv[2])).run()


if __name__ == "__main__":
    main()
