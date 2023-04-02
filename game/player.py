import random

class Player:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []

    def draw_pieces(self, count=2):
        drawn_pieces = random.sample(self.deck, count)
        self.hand.extend(drawn_pieces)
        for piece in drawn_pieces:
            self.deck.remove(piece)

    def play_piece(self, piece):
        if piece in self.hand:
            self.hand.remove(piece)
            return piece
        else:
            raise ValueError("La pieza no está en la mano del jugador.")

    def return_piece(self, piece):
        self.hand.remove(piece)
        self.deck.append(piece)
