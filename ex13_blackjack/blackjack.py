"""Simple game of blackjack."""
from textwrap import dedent
import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code

    def __repr__(self)-> str:
        """
        Card object representation in string format.

        :return: string
        """
        return f"{self.code}"


class Hand:
    """Simple class for holding hand information."""

    def __init__(self):
        """Constructor."""
        self.score = 0
        self.cards = []
        self.aces = 0

    def add_card(self, card: Card):
        """Add card."""
        self.add_score(card)
        self.cards.append(card)

    def add_score(self, card: Card):
        """Get player score."""
        aces_list = []
        if card.value.isdigit():
            self.score += int(card.value)
        if card.value == "ACE":
            self.aces += 1
            self.score += 11
        if card.value in ["JACK", "QUEEN", "KING"]:
            self.score += 10

        if self.score > 21 and self.aces > 0:
            for card in self.cards:
                aces_list.append(card.value)
            while self.score > 21 and self.aces != 0:
                self.score -= 10
                aces_list.remove("ACE")
                self.aces -= 1
        # if aces_list:
        #     for index, ace in enumerate(aces_list):
        #         if len(aces_list) - 1 != index or self.score + 11 > 21:
        #             self.score += 1
        #         else:
        #             self.score += 11


class Deck:
    """Deck of cards. Provided via api over the network."""

    def __init__(self, shuffle=False):
        """
        Tell api to create a new deck.

        :param shuffle: if shuffle option is true, make new shuffled deck.
        """
        if shuffle is False:
            self.deck = requests.get("https://deckofcardsapi.com/api/deck/new").json()
            self.deck_id = self.deck["deck_id"]
            self.is_shuffled = True
        if shuffle is True:
            self.deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle").json()
            self.deck_id = self.deck["deck_id"]
            self.is_shuffled = False

    def shuffle(self):
        """Shuffle the deck."""
        requests.get("https://deckofcardsapi.com/api/deck/{}/shuffle".format(self.deck_id))
        self.is_shuffled = True

    def draw(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        draw_card = requests.get("https://deckofcardsapi.com/api/deck/{}/draw".format(self.deck_id)).json()["cards"]
        return Card(draw_card[0]["value"], draw_card[0]["suit"], draw_card[0]["code"])


class BlackjackController:
    """Blackjack controller. For controlling the game and data flow between view and database."""

    def __init__(self, deck: Deck, view: 'BlackjackView'):
        """
        Start new blackjack game.

        :param deck: deck to draw cards from.
        :param view: view to communicate with.
        """
        self.state = {}
        self.deck = deck
        player = Hand()
        dealer = Hand()
        self.state["player"] = player
        self.state["dealer"] = dealer

        if not deck.is_shuffled:
            deck.shuffle()
        for i in range(2):
            player.add_card(deck.draw())
            dealer.add_card(deck.draw())

        self.play(player, dealer, deck, view)

    def play(self, player, dealer, deck: Deck, view: 'BlackjackView'):
        """Playing the game."""
        while True:
            if player.score > 21:
                view.player_lost(self.state)
                break
            if player.score == 21:
                view.player_won(self.state)
                break
            if player.score < 21:
                if view.ask_next_move(self.state) == "H":
                    player.add_card(deck.draw())
                else:
                    while True:
                        if dealer.score < player.score:
                            dealer.add_card(deck.draw())
                        else:
                            view.player_lost(self.state)
                            break
                        if dealer.score == 21:
                            view.player_lost(self.state)
                            break
                        elif dealer.score > 21:
                            view.player_won(self.state)
                            break



class BlackjackView:
    """Minimalistic UI/view for the blackjack game."""

    def ask_next_move(self, state: dict) -> str:
        """
        Get next move from the player.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :return: parsed command that user has choses. String "H" for hit and "S" for stand
        """
        self.display_state(state)
        while True:
            action = input("Choose your next move hit(H) or stand(S) > ")
            if action.upper() in ["H", "S"]:
                return action.upper()
            print("Invalid command!")

    def player_lost(self, state):
        """
        Display player lost dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You lost")

    def player_won(self, state):
        """
        Display player won dialog to the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        """
        self.display_state(state, final=True)
        print("You won")

    def display_state(self, state, final=False):
        """
        Display state of the game for the user.

        :param state: dict with given structure: {"dealer": dealer_hand_object, "player": player_hand_object}
        :param final: boolean if the given state is final state. True if game has been lost or won.
        """
        dealer_score = state["dealer"].score if final else "??"
        dealer_cards = state["dealer"].cards
        if not final:
            dealer_cards_hidden_last = [c.__repr__() for c in dealer_cards[:-1]] + ["??"]
            dealer_cards = f"[{','.join(dealer_cards_hidden_last)}]"

        player_score = state["player"].score
        player_cards = state["player"].cards
        print(dedent(
            f"""
            {"Dealer score":<15}: {dealer_score}
            {"Dealer hand":<15}: {dealer_cards}

            {"Your score":<15}: {player_score}
            {"Your hand":<15}: {player_cards}
            """
        ))


if __name__ == '__main__':
    BlackjackController(Deck(), BlackjackView())  # start the game.
