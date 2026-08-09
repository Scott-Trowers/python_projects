import random

class BeachRow:
    """ Converts the game screen into rows, to ensure crabs spawn in a grid """

    def __init__(self, screen_height, row_width):

        self.row_width = row_width
        self.n_rows = int(screen_height / row_width)

        self.rows = random.choices([-1, 1], k=self.n_rows)

        print(self.rows)
