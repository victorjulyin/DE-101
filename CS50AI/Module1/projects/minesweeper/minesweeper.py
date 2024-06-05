import itertools
import random

class Minesweeper():
    """
    Minesweeper game representation
    """
    def __init__(self, height=8, width=8, mines=8):
        self.height = height
        self.width = width
        self.mines = set()

        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        self.mines_found = set()

    def print(self):
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
        count = 0
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1
        return count

    def won(self):
        return self.mines_found == self.mines

class Sentence():
    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count
        self.initial_count = count
        self.mines = set()
        self.safes = set()

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        return self.mines

    def known_safes(self):
        return self.safes

    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        self.mines.add(cell)

    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
        self.safes.add(cell)

class MinesweeperAI():
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):
        self.mines.add(cell)
        print('in mark_mine in MinesweeperAI')
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # -------------------------------------
        # get all neighbour cells
        neighbour_cells = set()
        x_start = max(cell[0] - 1, 0)
        x_stop = min(cell[0] + 2, self.width)

        y_start = max(cell[1] - 1, 0)
        y_stop = min(cell[1] + 2, self.height)
        for i in range(x_start, x_stop):
            for j in range(y_start, y_stop):
                neighbour_cells.add((i, j))

        # -------------------------------------
        # exclude known mine cells from the sentence
        risked_cells = neighbour_cells - self.safes
        common_mine_cells = {i for i in self.mines if i in risked_cells}
        sentence_cells = risked_cells - common_mine_cells
        sentence_count = count - len(common_mine_cells)

        # -------------------------------------
        # if length of the sentence == count then mark all cells as mines
        # elif count == 0 then mark all cells as safes
        # else try to exclude existing sets from sentence and add a new sentence
        if len(sentence_cells) == sentence_count:
            for i in sentence_cells:
                self.mark_mine(i)
        elif sentence_count == 0:
            for i in sentence_cells:
                self.mark_safe(i)
        else:
            for kb_sentence in self.knowledge:
                kb_sentence_cells = kb_sentence.cells
                kb_sentence_count = kb_sentence.count
                if all(i in sentence_cells for i in kb_sentence_cells):
                    sentence_cells = sentence_cells - kb_sentence_cells
                    sentence_count = sentence_count - kb_sentence_count
            new_sentence = Sentence(sentence_cells, sentence_count)
            self.knowledge.append(new_sentence)
            print(f"New knowledge added: {new_sentence}")

        # -------------------------------------
        # try to exclude existing sets from different existing sentences
        for sentence1 in self.knowledge:
            other_sentences = self.knowledge.copy()
            other_sentences.remove(sentence1)
            for sentence2 in other_sentences:
                sentence2_cells = sentence2.cells
                sentence1_cells = sentence1.cells
                if all(i in sentence1_cells for i in sentence2_cells):
                    sentence1.cells = sentence1.cells - sentence2.cells
                    sentence1.count = sentence1.count - sentence2.count

        # -------------------------------------
        # get new mines and safes in the KB and mark them
        mines_to_add = set()
        safes_to_add = set()
        for sentence in self.knowledge:
            if sentence.count == len(sentence.cells):
                print('found sentence with mines')
                print(f'{sentence.cells} = {sentence.count}')
                for i in sentence.cells:
                    mines_to_add.add(i)
            elif sentence.count == 0 and len(sentence.cells) != 0:
                print('found sentence with safes')
                print(f'{sentence.cells} = {sentence.count}')
                for i in sentence.cells:
                    safes_to_add.add(i)

        for i in mines_to_add:
            self.mark_mine(i)
        for i in safes_to_add:
            self.mark_safe(i)

        # -------------------------------------
        # sort knowledge to prioritize the moves that can give more info
        sorted_knowledge = sorted(self.knowledge, key=lambda x: x.initial_count, reverse=True)
        sorted_knowledge = [sentence for sentence in sorted_knowledge if sentence.cells != set()]
        self.knowledge = sorted_knowledge

        print("Current knowledge base:")
        for sentence in self.knowledge:
            print(sentence)

        print('--------------------------------------')
        print('all safes')
        print(self.safes)
        print('--------------------------------------')
        print('all mines')
        print(self.mines)
        print('--------------------------------------')
        print('--------------------------------------')
        print('--------------------------------------')


    def make_safe_move(self):
        cells = self.safes - self.moves_made
        if cells:
            l = list(cells)
            return random.choice(l)
        else:
            return None

    def make_random_move(self):
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
