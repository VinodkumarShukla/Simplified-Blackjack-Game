import random

def main():
    print("Welcome to Simplified Blackjack!")

    while True:
        player_score = get_player_score()
        if player_score > 21:
            print("You BUSTED with a total value of 25!")
            print("** You lose. **")
        else:
            dealer_score = get_dealer_score()
            print(f"The dealer was dealt a hand with a value of {dealer_score}")

            if dealer_score > 21 or player_score > dealer_score:
                print("** You win! **")
            elif player_score == dealer_score:
                print("It's a tie!")
            else:
                print("** You lose. **")

        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != "y":
            break

def get_player_score():
    x = deal_card()
    y = deal_card()
    sum = x + y
    print(f"Your hand of two cards has a total value of {sum}")

    while sum <= 21:
        choice = input("Would you like to take another card? (y/n) ").lower()
        if choice == "y":
            card = deal_card()
            sum += card
            print(f"Your hand now has a total value of {sum}")
        else:
            print(f"You have stopped taking more cards with a hand value of {sum}.")
            break

    return sum

def deal_card():
    # Make 10s four times more likely than other values
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1]  # 1 represents Ace
    return random.choice(card_values)

def get_dealer_score():
    dealer_hand = [deal_card(), deal_card()]
    dealer_score = sum(dealer_hand)

    while dealer_score < 16:
        card = deal_card()
        dealer_hand.append(card)
        dealer_score += card

    return dealer_score

if __name__ == "__main__":
    main()
