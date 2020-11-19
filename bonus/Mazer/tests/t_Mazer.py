############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

import pytest


from sources.Mazer import Mazer
from tests.deps.expected import *


def test_normal_case(capsys):

    argv = ['./mazer', '10', '10']
    argMan = Mazer(argv[1], argv[2]).run()

    redir = capsys.readouterr()
    assert redir.out != ""
