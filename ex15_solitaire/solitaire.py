"""Golf solitaire."""
from itertools import zip_longest
from textwrap import dedent
from cards import Deck


class Solitaire:
    """
    Solitaire class representing a game of Golf Solitaire.

    This game has 7 columns and 5 cards in each column,
    but the methods should work with other valid values as well.
    """

    columns = 7
    cards_in_column = 5

    def __init__(self):
        """
        Constructor, do the setup here.

        After setup with Solitaire.columns = 7, Solitaire.cards_in_column = 5
        You should have:
        self.tableau -> 7 columns of cards with 5 cards in each column
        self.stock -> 16 cards
        self.waste -> 1 card
        """
        self.deck = Deck()  # -> Deck instance
        self.tableau = []  # -> list of (columns[lists] (where each list -> cards_in_column * Card instances))
        self.waste = []  # -> list of Card instances
        self.stock = []  # -> list of Card instances
        self.deck.shuffle_deck()  # ->  shuffle_deck() from package cards
        for column in range(self.columns):
            column = []
            for card in range(self.cards_in_column):
                column.append(self.deck.deal_card())  # -> deal_card() from package cards
            self.tableau.append(column)
        self.waste.append(self.deck.deal_card())
        for card in range(len(self.deck.cards)):
            self.stock.append(self.deck.deal_card())

    def can_move(self, card) -> bool:
        """
        Validate if a card from the tableau can be moved to the waste pile.

        The card must be last in the column list and adjacent by rank
        to the topmost card of the waste pile (last in waste list).
        Example: 8 is adjacent to 7 and 9. Ace is only adjacent to 2.
        King is only adjacent to Queen.
        """
        if card in [card[-1] for card in self.tableau if card]:
            return abs(card.rank - self.waste[-1].rank) == 1
        return False

    def move_card(self, col: int):
        """
        Move a card from the tableau to the waste pile.

        Does not validate the move.
        :param col: index of column
        """
        if self.tableau[col]:
            self.waste.append(self.tableau[col].pop(-1))

    def deal_from_stock(self):
        """
        Deal last card from stock pile to the waste pile.

        If the stock is empty, do nothing.
        """
        if self.stock:
            self.waste.append(self.stock.pop(-1))

    def has_won(self) -> bool:
        """Check for the winning position - no cards left in tableau."""
        return all(not card for card in self.tableau)

    def has_lost(self) -> bool:
        """
        Check for the losing position.

        Losing position: no cards left in stock and no possible moves.
        """
        return not self.stock and all(not self.can_move(card) for card in [card[-1] for card in self.tableau if card])

    def print_game(self):
        """
        Print the game.

        Assumes:
        Card(decorated=True) by default it is already set to True
        self.tableau -> a list of lists (each list represents a column of cards)
        self.stock -> a list of Card objects that are in the stock
        self.waste_pile -> a list of Card objects that are in the waste pile

        You may modify/write your own print_game.
        """
        print(f" {'    '.join(list('0123456'))}")
        print('-' * 34)
        print("\n".join([(" ".join((map(str, x)))) for x in (zip_longest(*self.tableau, fillvalue="    "))]))
        print()
        print(f"Stock pile: {len(self.stock)} card{'s' if len(self.stock) != 1 else ''}")
        print(f"Waste pile: {self.waste[-1] if self.waste else 'Empty'}")

    @staticmethod
    def rules():
        """Print the rules of the game."""
        print("Rules".center(40, "-"))
        print(dedent("""
                Objective: Move all the cards from each column to the waste pile.

                A card can be moved from a column to the waste pile if the
                rank of that card is one higher or lower than the topmost card
                of the waste pile. Only the first card of each column can be moved.

                You can deal cards from the stock to the waste pile.
                The game is over if the stock is finished and
                there are no more moves left.

                The game is won once the tableau is empty.

                Commands:
                  (0-6) - integer of the column, where the topmost card will be moved
                  (d) - deal a card from the stock
                  (r) - show rules
                  (q) - quit
                  """))

    def play(self):
        """
        Play a game of Golf Solitaire.

        Create the game loop here.
        Use input() for player input.
        Available commands are described in rules().
        """
        while True:
            command = self.ask_next_move()
            if command == "q":
                break
            if command == "r":
                self.rules()
            if command == "d":
                self.deal_from_stock()
            if command in (0, 1, 2, 3, 4, 5, 6):
                if self.can_move(self.tableau[command][-1]):
                    self.move_card(command)
                else:
                    print("Invalid move! Try again!")
            if not self.stock:
                if self.has_lost():
                    print("No more moves left! You lost!")
                    break
                if self.has_won():
                    print("Congratulations! You won!")
                    break

    def ask_next_move(self):
        """Next move from the player."""
        self.print_game()
        while True:
            action = input("Choose your next move > ")
            if action in ["0", "1", "2", "3", "4", "5", "6"]:
                return int(action)
            if action in ["d", "r", "q"]:
                return action
            print("Invalid command!")


if __name__ == '__main__':
    s = Solitaire()
    s.play()
