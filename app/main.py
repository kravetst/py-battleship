class Deck:
    def __init__(
            self, row: int,
            column: int,
            is_alive: bool = True
    ) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self,
                 start: tuple[int, int],
                 end: tuple[int, int],
                 is_drowned: bool = False
                 ) -> None:

        self.start = start
        self.end = end
        self.is_drowned = is_drowned
        self.decks = []

        if self.start[0] == self.end[0]:    # рядок однаковий
            # Horizontal
            for col in range(
                    min(self.start[1], self.end[1]),
                    max(self.start[1], self.end[1]) + 1
            ):

                deck = Deck(self.start[0], col)
                self.decks.append(deck)
        elif self.start[1] == self.end[1]:   # стовпчик однаковий
            # Vertical
            for row in range(
                    min(self.start[0], self.end[0]),
                    max(self.start[0], self.end[0]) + 1
            ):

                deck = Deck(row, self.start[1])
                self.decks.append(deck)

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck

    def fire(self, row: int, column: int) -> None:
        deck = self.get_deck(row, column)
        if deck is not None:
            deck.is_alive = False

        if all(not d.is_alive for d in self.decks):
            self.is_drowned = True


class Battleship:
    def __init__(
            self,
            ships: list[tuple[tuple[int, int], tuple[int, int]]]
    ) -> None:
        self.ships = []
        self.field = {}
        for start, end in ships:
            ship = Ship(start, end)
            self.ships.append(ship)
            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple[int, int]) -> str:
        if location not in self.field:
            return "Miss!"
        row, column = location
        ship = self.field[location]
        ship.fire(row, column)
        if ship.is_drowned:
            return "Sunk!"
        else:
            return "Hit!"
        # This function should check whether the location
        # is a key in the `self.field`
        # If it is, then it should check if this cell is the last alive
        # in the ship or not.
