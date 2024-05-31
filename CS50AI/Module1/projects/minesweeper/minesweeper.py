import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count


################################
        self.mines = set()
        self.safes = set()
################################

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.mines

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        return self.safes

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

        self.mines.add(cell)

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        print('--------------------------')
        print('mark_safe in Sentence')
        print('self.cells')
        print(self.cells)

        print('self.count')
        print(self.count)

        print('cell')
        print(cell)
        print('--------------------------')

        if cell in self.cells:
            self.cells.remove(cell)
        self.safes.add(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)

        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # ------------------------------------------------
        # 1) mark the cell as a move that has been made
        self.moves_made.add(cell)

        # ------------------------------------------------
        # 2) mark the cell as safe
        self.mark_safe(cell)

        # ------------------------------------------------
        # 3) add a new sentence to the AI's knowledge base
        #     based on the value of `cell` and `count`

        # 3.1) get all neighbour cells
        neighbour_cells = set()
        x_start = max(cell[0] - 1, 0)
        x_stop = min(cell[0] + 2, self.width)

        y_start = max(cell[1] - 1, 0)
        y_stop = min(cell[1] + 2, self.height)
        for i in range(x_start, x_stop):
            for j in range(y_start, y_stop):
                neighbour_cells.add((i, j))

        # 3.2) filter out common mine cells
        risked_cells = neighbour_cells - {cell} - self.safes
        common_mine_cells = {i for i in self.mines if i in risked_cells}

        sentence_cells = risked_cells - common_mine_cells
        sentence_count = count - len(common_mine_cells)

        # ------------------------------------------------
        # 4) mark any additional cells as safe or as mines
        #     if it can be concluded based on the AI's knowledge base
        if len(sentence_cells) == sentence_count:
            for i in sentence_cells:
                self.mark_mine(i)
        elif sentence_count == 0:
            for i in sentence_cells:
                self.mark_safe(i)

        # ------------------------------------------------
        # 5) add any new sentences to the AI's knowledge base
        #     if they can be inferred from existing knowledge
        for sentence in self.knowledge:
            if sentence.cells in sentence_cells:
                sentence_cells = sentence_cells - sentence.cells
                sentence_count = sentence_count - sentence.count

        self.knowledge.append(Sentence(sentence_cells, sentence_count))



       # raise NotImplementedError

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        cells = self.safes - self.moves_made
        if cells:
            l = list(cells)
            return random.choice(l)
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        cells = set()
        for i in range(self.width):
            for j in range(self.height):
                cells.add((i, j))

        cells = cells - self.mines - self.moves_made

        if cells:
            l = list(cells)
            return random.choice(l)
        else:
            return None
