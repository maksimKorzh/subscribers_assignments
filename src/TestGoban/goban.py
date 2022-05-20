import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """

    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban
        
        # liberties list, needed to check whether a stone is taken or not
        self.liberties = []
        
        # traversed stones of a single group, needed to avoid endless recursion
        self.traversed = []

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if (
            not self.goban
            or x < 0
            or y < 0
            or y >= len(self.goban)
            or x >= len(self.goban[0])
        ):
            return Status.OUT
        elif self.goban[y][x] == ".":
            return Status.EMPTY
        elif self.goban[y][x] == "o":
            return Status.WHITE
        elif self.goban[y][x] == "#":
            return Status.BLACK

    def is_taken(self, x, y, color):
        """
        Get the capture status of the given stone
        
        Args:
            x: the x coordinate
            y: the y coordinate
            color: color of the stone to check
        
        Returns:
            True if stone is captured
            False otherwise
        """
        # clear traversed stones and liberties every next run
        self.liberties = []
        self.traversed = []
        
        # count liberties for a stone/group, this populates liberties list if any
        self.count(x, y, color)
        
        # if stone/group has at least one liberty
        if len(self.liberties):
            # it means it's not captured
            return False
        
        # if stone/group doesn't have any liberties
        else:
            # it means it's captured
            return True

    def count(self, x, y, color):
        """
        Recursively traverses the group of stones and counts liberties
        
        Args:
            x: the x coordinate
            y: the y coordinate
            color: color of the stone to check
        
        Returns:
            None
        """
        # get board square/piece status (it might be white, black, empty or offboard)
        piece = self.get_status(x, y)
                
        # skip offboard squares (this also treats them as non-empty)
        if piece == Status.OUT: return
        
        # if more than one stone found within a group
        if piece != Status.EMPTY and piece == color and (x, y) not in self.traversed:
            # store previously traversed square
            self.traversed.append((x, y))
            
            # look for neighbours recursively
            self.count(x, y - 1, color)             # walk north
            self.count(x - 1, y, color)             # walk east
            self.count(x, y + 1, color)             # walk south
            self.count(x + 1, y, color)             # walk west

        # if the square is empty
        elif piece == Status.EMPTY:
            # store liberty
            self.liberties.append((x, y))
        
        
