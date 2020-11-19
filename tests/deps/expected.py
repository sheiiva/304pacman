############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#            Project : 304pacman           #
#                                          #
############################################


HELP_MESSAGE = "\
./304pacman file c1 c2\n\
\tfile\tfile describing the board, using the following characters:\n\
\t\t\t‘0’ for an empty square,\n\
\t\t\t‘1’ for a wall,\n\
\t\t\t‘F’ for the ghost’s position,\n\
\t\t\t‘P’ for Pacman’s position.\n\
\tc1\tcharacter to display for a wall\n\
\tc2\tcharacter to display for an empty space.\n"

MAP1_OUTPUT = "\
++++++++++\n\
          \n\
     2    \n\
    212   \n\
    1F12  \n\
     12   \n\
     P    \n\
          \n\
          \n\
++++++++++"

MAP2_OUTPUT = "\
@@@@@@@@@@@@@@@\n\
@      @109890@\n\
@ @ @@8@0@@7@9@\n\
@  P767@987678@\n\
@ @ @5@@@7@5@7@\n\
@ @8@43@765456@\n\
@ @7@@2@8@@3@@@\n\
@@@6@21090@2@@@\n\
@765432101@1F1@\n\
@8@6@43212@2@@@\n\
@@@7@5@@@@@3@@@\n\
@  876@@765456@\n\
@ @@@7@@8@6@@7@\n\
@  @ 8 @987@98@\n\
@@   @@@0@8@0@@\n\
@  @   @109012@\n\
@ @@@7@@2@@@@3@\n\
@ @ @654345654@\n\
@@@@@@@@@@@@@@@"

MAP_NOPATH_OUTPUT ="\
++++++++++\n\
          \n\
          \n\
    +++   \n\
    +F+   \n\
    +++   \n\
     P    \n\
          \n\
          \n\
++++++++++"
