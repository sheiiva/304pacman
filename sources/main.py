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
from sources.Pacman import Pacman


def main():

    argsManager = ArgumentManager()

    if argsManager.needHelp(argv):
        Usage()
    elif argsManager.checkArgs(argv) == 84:
        exit(84)
    else:
        Pacman(argv[2], argv[3]).run(argv[1])


if __name__ == "__main__":
    main()
