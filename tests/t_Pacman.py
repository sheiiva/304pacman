############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

from sources.Pacman import Pacman
from tests.deps.expected import *


def test_normal_case(capsys):

    argv = ['./304pacman', 'tests/deps/map1', '+', ' ']
    argMan = Pacman(argv[2], argv[3]).run(argv[1])

    redir = capsys.readouterr()
    assert redir.out == "{}\n".format(MAP1_OUTPUT)


def test_tricky_case(capsys):

    argv = ['./304pacman', 'tests/deps/map2', '@', ' ']
    argMan = Pacman(argv[2], argv[3]).run(argv[1])

    redir = capsys.readouterr()
    assert redir.out == "{}\n".format(MAP2_OUTPUT)


def test_no_pacman(capsys):

    argv = ['./304pacman', 'tests/deps/mapNoPacman', '+', ' ']

    try:
        argMan = Pacman(argv[2], argv[3]).run(argv[1])
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "No pacman in map.\n"
    else:
        assert True is False    # Test has failed


def test_no_ghost(capsys):

    argv = ['./304pacman', 'tests/deps/mapNoGhost', '+', ' ']

    try:
        argMan = Pacman(argv[2], argv[3]).run(argv[1])
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "No ghost in map.\n"
    else:
        assert True is False    # Test has failed


def test_normal_nopath(capsys):

    argv = ['./304pacman', 'tests/deps/map_nopath', '+', ' ']
    argMan = Pacman(argv[2], argv[3]).run(argv[1])

    redir = capsys.readouterr()
    assert redir.out == "{}\n".format(MAP_NOPATH_OUTPUT)


def test_several_ghosts(capsys):

    argv = ['./304pacman', 'tests/deps/map2ghosts', '+', ' ']

    try:
        argMan = Pacman(argv[2], argv[3]).run(argv[1])
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "Too many ghosts.\n"
    else:
        assert True is False    # Test has failed


def test_several_pacmen(capsys):

    argv = ['./304pacman', 'tests/deps/map2pacmen', '+', ' ']

    try:
        argMan = Pacman(argv[2], argv[3]).run(argv[1])
    except SystemExit:
        redir = capsys.readouterr()
        assert redir.out == "Too many pacmans.\n"
    else:
        assert True is False    # Test has failed
