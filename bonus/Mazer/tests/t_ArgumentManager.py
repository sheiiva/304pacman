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

    argv = ['./304pacman', '4', '4']

    assert argMan.checkArgs(argv) == 0

def test_needHelp_h():

    argMan = ArgumentManager()

    argv = ['./304pacman', '-h']

    assert argMan.needHelp(argv) is True


def test_needHelp_help():

    argMan = ArgumentManager()

    argv = ['./304pacman', '--help']

    assert argMan.needHelp(argv) is True


def test_dont_needHelp():

    argMan = ArgumentManager()

    argv = ['./304pacman', 'nohelp']

    assert argMan.needHelp(argv) is False


def test_wrong_number_args(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'args']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Wrong number of arguments.\n"


def test_first_not_digit(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'a', '10']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Please enter correct size for the map.\n"


def test_second_not_digit(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', '10', 'a']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Please enter correct size for the map.\n"


def test_both_not_digit(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', 'a', 'a']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Please enter correct size for the map.\n"


def test_first_wrong_value(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', '1', '10']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Size required is too little. Try with bigger values.\n"


def test_second_wrong_value(capsys):

    argMan = ArgumentManager()

    argv = ['./304pacman', '10', '1']

    assert argMan.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "Size required is too little. Try with bigger values.\n"
