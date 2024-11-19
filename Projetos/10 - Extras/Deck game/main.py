import tkinter as tk
from tkinter import ttk
import random

class Card:
    """
    Represents a single card with a suit and a value.
    """
    def __init__(self, suit, value):
        """
        Initializes the card with a suit and value.

        Args:
            suit (str): The suit of the card (e.g., 'Copas', 'Ouros').
            value (str): The value of the card (e.g., 'Ás', '2', 'Valete').
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: The card's value and suit (e.g., "Ás de Copas").
        """
        return f"{self.value} de {self.suit}"

    def numeric_value(self):
        """
        Gets the numerical value of the card for game scoring purposes.

        Returns:
            int: The card's numerical value (e.g., Ace = 11, face cards = 10).
        """
        if self.value == 'Ás':
            return 11  # Ace can be worth 11
        elif self.value in ['Valete', 'Dama', 'Rei']:
            return 10  # Face cards are worth 10
        else:
            return int(self.value)  # Number cards are worth their own value

class Deck:
    """
    Represents a deck of cards, which can be shuffled and drawn from.
    """
    def __init__(self):
        """
        Initializes the deck with 52 cards and shuffles it.
        """
        suits = ['Copas', 'Ouros', 'Espadas', 'Paus']
        values = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)  # Shuffle the deck

    def draw_card(self):
        """
        Draws a card from the deck if available.

        Returns:
            Card: A card from the deck, or None if the deck is empty.
        """
        return self.cards.pop() if self.cards else None  # Returns None if no more cards

class CardGame:
    """
    Represents the card game interface and game logic.
    """
    def __init__(self):
        """
        Initializes the game window and elements, and sets up the game deck.
        """
        self.window = tk.Tk()
        self.window.title("Jogo de Cartas")
        self.window.geometry("800x400")
        self.window.resizable(False, False)
        self.deck = Deck()  # Initializes the deck
        self.player_cards = []
        self.cpu_cards = []
        self.init_ui()

    def init_ui(self):
        """
        Sets up the game UI elements, including buttons and labels.
        """
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Start button
        self.start_button = ttk.Button(main_frame, text="Iniciar Jogo", command=self.start_game)
        self.start_button.grid(row=0, column=0, pady=10)

        # Player's card label
        self.player_card_label = ttk.Label(main_frame, text="", font=("Arial", 12))
        self.player_card_label.grid(row=1, column=0, pady=10)

        # CPU's card label
        self.cpu_card_label = ttk.Label(main_frame, text="", font=("Arial", 12))
        self.cpu_card_label.grid(row=4, column=0, pady=10)

        # Draw card button
        self.draw_button = ttk.Button(main_frame, text="+1", command=self.draw_one_more, state=tk.DISABLED)
        self.draw_button.grid(row=2, column=0, pady=10)

        # Stop button
        self.stop_button = ttk.Button(main_frame, text="Parar", command=self.stop_game, state=tk.DISABLED)
        self.stop_button.grid(row=3, column=0, pady=10)

    def start_game(self):
        """
        Starts a new game by resetting player and CPU cards, and enabling buttons.
        """
        print("Jogo iniciado!")
        self.player_cards = []
        self.cpu_cards = []
        self.draw_one_more()
        self.draw_one_more()
        self.draw_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def draw_one_more(self):
        """
        Draws a card for the player and updates the display. Checks if the player busts (goes over 21).
        """
        drawn_card = self.deck.draw_card()  # Draws a card from the deck
        if drawn_card:
            self.player_cards.append(drawn_card)  # Adds the card to player's hand
            self.update_player_card_label()
            if self.calculate_total(self.player_cards) > 21:
                self.player_card_label.config(text="Você estourou! Perdeu.")
                self.draw_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.DISABLED)
        else:
            self.player_card_label.config(text="Não há mais cartas no baralho.")

    def stop_game(self):
        """
        Stops the player's turn and starts the CPU's turn.
        """
        self.cpu_card_label.config(text="CPU está puxando cartas...")
        self.cpu_draw_cards()

    def cpu_draw_cards(self):
        """
        Draws cards for the CPU until it reaches 17 or more points, then checks for the winner.
        """
        if self.calculate_total(self.cpu_cards) < 17:  # CPU draws until it has 17 or more
            cpu_card = self.deck.draw_card()
            if cpu_card:
                self.cpu_cards.append(cpu_card)
                self.update_cpu_card_label()
                self.window.after(1000, self.cpu_draw_cards)  # Waits 1 second before drawing next card
            else:
                self.determine_winner()  # Checks the winner if no more cards are available
        else:
            self.determine_winner()  # Checks the winner if CPU has 17 or more

    def determine_winner(self):
        """
        Determines the winner based on the player's and CPU's card totals, and updates the display.
        """
        player_total = self.calculate_total(self.player_cards)
        cpu_total = self.calculate_total(self.cpu_cards)

        if cpu_total > 21:
            self.player_card_label.config(text="CPU estourou! Você ganhou!")
        elif player_total > 21:
            self.player_card_label.config(text="Você estourou! Perdeu.")
        elif player_total > cpu_total:
            self.player_card_label.config(text="Você ganhou!")
        elif player_total < cpu_total:
            self.player_card_label.config(text="CPU ganhou!")
        else:
            self.player_card_label.config(text="Empate!")

    def calculate_total(self, cards):
        """
        Calculates the total value of a hand of cards, adjusting for aces if necessary.

        Args:
            cards (list of Card): The list of cards in the hand.

        Returns:
            int: The total value of the hand.
        """
        total = 0
        aces = 0
        for card in cards:
            total += card.numeric_value()
            if card.value == 'Ás':
                aces += 1
        # Adjust the value of aces if total is over 21
        while total > 21 and aces:
            total -= 10  # Count Ace as 1 instead of 11
            aces -= 1
        return total

    def update_player_card_label(self):
        """
        Updates the display to show the player's current hand and total value.
        """
        cards_str = ', '.join(str(card) for card in self.player_cards)
        self.player_card_label.config(text=f"Suas cartas: {cards_str} (Total: {self.calculate_total(self.player_cards)})")

    def update_cpu_card_label(self):
        """
        Updates the display to show the CPU's current hand and total value.
        """
        cards_str = ', '.join(str(card) for card in self.cpu_cards)
        self.cpu_card_label.config(text=f"Cartas da CPU: {cards_str} (Total: {self.calculate_total(self.cpu_cards)})")

    def run(self):
        """
        Runs the main loop of the Tkinter application.
        """
        self.window.mainloop()

if __name__ == "__main__":
    game = CardGame()
    game.run()
