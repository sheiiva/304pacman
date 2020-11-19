############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################

class Usage():

    def __init__(self):
        self.show()

    def show(self) -> None:

        """
        Show usage of the program.
        """

        print(
            "./mazer length width\n"
            "\n"
            "\tlength\tlength of the map.\n"
            "\twidth\twidth of the map."
            )
