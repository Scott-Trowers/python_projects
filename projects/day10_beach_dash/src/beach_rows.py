import random

class BeachRow:
    def __init__(self, screen_height, row_width):

        self.row_width = row_width
        self.n_rows = int(screen_height / row_width)

        self.rows = random.choices([-1, 1], k=self.n_rows)

        print(self.rows)
