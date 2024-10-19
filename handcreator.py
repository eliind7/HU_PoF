from treys import Deck, Evaluator, Card


deck = Deck()

# Deal two hands for two players (heads-up)
# Unpack the card integers from the lists
player1_hand = deck.draw(2) # Unpack the integer from the list
player2_hand = deck.draw(2)

# Deal the board (community cards)
community_cards = deck.draw(5)

# Print the cards for each player
print("Player 1 hand:")
Card.print_pretty_cards(player1_hand)
print("\nPlayer 2 hand:")
Card.print_pretty_cards(player2_hand)

# Print the community cards
print("\nCommunity cards:")
Card.print_pretty_cards(community_cards)

# Evaluator to determine hand strength
evaluator = Evaluator()

# Evaluate the hands (smaller number is better)
player1_score = evaluator.evaluate(player1_hand, community_cards)
player2_score = evaluator.evaluate(player2_hand, community_cards)

# Determine the winner
print(f"Player 1 hand score: {player1_score}")
print(f"Player 2 hand score: {player2_score}")

if player1_score < player2_score:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
