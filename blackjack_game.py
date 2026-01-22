import random

# ---------------------------
# Card and Deck Setup
# ---------------------------
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    """Create a deck of 52 cards as (rank, suit) tuples."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# ---------------------------
# Hand Value Calculation
# ---------------------------
def hand_value(hand):
    """Calculate the total value of a hand, counting Aces as 11 or 1."""
    value = 0
    aces = 0
    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    # Adjust for Aces if total > 21
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

# ---------------------------
# Display Hands
# ---------------------------
def display_hands(player, dealer, hide_dealer=True):
    print("\nPlayer's Hand:", player, "Value:", hand_value(player))
    if hide_dealer:
        print("Dealer's Hand: [??,", dealer[1], "]")
    else:
        print("Dealer's Hand:", dealer, "Value:", hand_value(dealer))

# ---------------------------
# Player Turn
# ---------------------------
def player_turn(deck, player):
    while True:
        display_hands(player, dealer)
        if len(player) == 5:
            print("5-Card Charlie! You win!")
            return True  # automatic win
        if hand_value(player) > 21:
            print("Busted! You lose!")
            return False
        move = input("Hit or Stay? (H/S): ").upper()
        if move == 'H':
            player.append(deck.pop())
        elif move == 'S':
            return None  # continue to dealer
        else:
            print("Enter H or S only.")

# ---------------------------
# Dealer Turn
# ---------------------------
def dealer_turn(deck, dealer):
    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
    display_hands(player, dealer, hide_dealer=False)
    if hand_value(dealer) > 21:
        print("Dealer busts! You win!")
        return True
    return None

# ---------------------------
# Game Setup
# ---------------------------
deck = create_deck()
player = [deck.pop(), deck.pop()]
dealer = [deck.pop(), deck.pop()]

# ---------------------------
# Game Play
# ---------------------------
# Player turn
result = player_turn(deck, player)
if result is True:
    pass  # player already won
elif result is False:
    pass  # player busted
else:
    # Dealer turn
    result = dealer_turn(deck, dealer)
    if result is True:
        pass  # dealer busted, player wins
    else:
        # Compare hands
        player_val = hand_value(player)
        dealer_val = hand_value(dealer)
        if player_val > dealer_val:
            print("You win!")
        elif player_val < dealer_val:
            print("You lose!")
        else:
            print("Push! It's a tie!")
