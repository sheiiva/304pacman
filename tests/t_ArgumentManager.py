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

from sources.ArgumentManager import ArgumentManager


def test_normal_case():

    argMan = ArgumentManager()

    argv = ['./304pacman', 'tests/deps/map1', '+', ' ']

    assert argMan.checkArgs(argv) == 0


def test_wrong_number_args(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'tests/deps/map1', ' ']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Wrong number of arguments.\n"


def test_not_a_file(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'notAFile', '+', ' ']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "notAFile is not a valid file.\n"


def test_empty_file(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'tests/deps/emptyFile', '+', ' ']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "tests/deps/emptyFile is empty.\n"


def test_same_char(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'tests/deps/map1', '+', '+']
    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Please enter different values for `c1` and `c2`.\n"


def test_needHelp_h():

    argMan = ArgumentManager()

    argv = ['./304pacman', '-h']

    assert argMan.needHelp(argv) is True


def test_needHelp_help():

    argMan = ArgumentManager()

    argv = ['./304pacman', '--help']

    assert argMan.needHelp(argv) is True


def test_needHelp_wrong_case():

    argMan = ArgumentManager()

    argv = ['./304pacman', 'no']

    assert argMan.needHelp(argv) is False
