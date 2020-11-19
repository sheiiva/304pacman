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
from random import choice, random

# DIFFICULTY PERCENTAGE (0 <==> IMPOSSIBLE)
MAPLEVEL = 80

class Character():

    def __init__(self, token: str):
        self._x = -1
        self._y = -1
        self._c = token

class Mazer():

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def create(self) -> list:
        """Create a map size as self._length*self._width

        Returns:
            list: [description]
        """
        return [[0 for _ in range(self._length)] for _ in range(self._width)]

    def fill(self, maze: list, pacman: Character, ghost: Character) -> None:
        """Place pacman, ghost and some walls in the maze.

        Args:
            maze (list): Maze to fill.
            pacman (Character): Pacman Character.
            ghost (Character): Ghost Character.
        """
        
        # PLACE CHARACTERS
        maze[pacman._y][pacman._x] = pacman._c
        maze[ghost._y][ghost._x] = ghost._c
        # PLACE WALLS
        for j in range(len(maze)):
            for i in range(len(maze[j])):
                if j == 0 or j == len(maze)-1:
                    maze[j][i] = 1
                if i == 0 or i == len(maze[j])-1:
                    maze[j][i] = 1
                if maze[j][i] != pacman._c and maze[j][i] != ghost._c:
                    if (random()*100) > MAPLEVEL:
                        maze[j][i] = 1

    def print(self, maze: list) -> None:
        """Print the input maze.

        Args:
            maze (list): Maze to print.
        """

        for line in maze:
            for elem in line:
                print(elem, end='')
            print()

    def placeCharacters(self, pacman: Character, ghost: Character) -> None:
        """Place pacman and ghost in the map.

        Args:
            pacman (Character): Pacman Character.
            ghost (Character): Ghost Character.
        """

        lengthList = range(1, self._length-1)
        widthList = range(1, self._width-1)

        # PLACE PACMAN
        pacman._x = choice(lengthList)
        pacman._y = choice(widthList)
        # PLACE GHOST
        ghost._x = choice(lengthList)
        ghost._y = choice(widthList)
        while ghost._x == pacman._x and ghost._y == pacman._y:
            # MOVE GHOST
            ghost._x = choice(lengthList)
            ghost._y = choice(widthList)

    def run(self):

        # CREATE
        maze = self.create()
        # CREATE CHARACTERS
        pacman = Character('P')
        ghost = Character('F')
        self.placeCharacters(pacman, ghost)
        # SET
        self.fill(maze, pacman, ghost)
        # PRINT
        self.print(maze)
