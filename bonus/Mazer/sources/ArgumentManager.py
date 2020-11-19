############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:
        """
        Check for input arguments validity.
        """

        def isDigit(elem) -> bool:
            try:
                int(elem)
            except ValueError:
                return False
            else:
                return True

        if len(argv) != 3:
            print("Wrong number of arguments.")
            return 84
        if isDigit(argv[1]) is False or isDigit(argv[2]) is False:
            print("Please enter correct size for the map.")
            return 84
        if int(argv[1]) < 4 or int(argv[2]) < 4:
            print("Size required is too little. Try with bigger values.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:
        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
