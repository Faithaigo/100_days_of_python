import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True

player_cards = []
player_score = 0

dealer_cards = []
dealer_score = 0

while is_playing:
    is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if is_play == 'n':
        is_playing = False
        print('Game over')
    else:
        player_numbers = [random.choice(cards), random.choice(cards)]
        player_cards += player_numbers
        player_score = sum(player_cards)

        dealer_first_card = random.choice(cards)
        dealer_cards.append(dealer_first_card)
        dealer_score = sum(dealer_cards)

        accept_play = True

        while accept_play:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {dealer_first_card}")

            draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if draw_card == 'y':
                player_cards.append(random.choice(cards))
                player_score = sum(player_cards)

                if player_score > 21:
                    print(f"Your final hand:{player_cards}, final score: {player_score}")
                    print(f"Computer's final hand:{dealer_cards}, final score: {dealer_score}")
                    print("You went over. You lose ")
                    player_cards = []
                    player_score = 0
                    dealer_cards = []
                    dealer_score = 0
                    accept_play = False
            else:
                computer_turn = True
                while computer_turn:
                    dealer_cards.append(random.choice(cards))
                    dealer_score = sum(dealer_cards)
                    if dealer_score > 17:
                        if dealer_score > 21:
                            print(f"Your final hand:{player_cards}, final score: {player_score}")
                            print(f"Computer's final hand:{dealer_cards}, final score: {dealer_score}")
                            print("Opponent went over. You win")
                            player_cards = []
                            player_score = 0
                            dealer_cards = []
                            dealer_score = 0
                            computer_turn = False
                            accept_play = False
                        elif dealer_score > player_score:
                            print(f"Your final hand:{player_cards}, final score: {player_score}")
                            print(f"Computer's final hand:{dealer_cards}, final score: {dealer_score}")
                            print("You lose")
                            player_cards = []
                            player_score = 0
                            dealer_cards = []
                            dealer_score = 0
                            computer_turn = False
                            accept_play = False
                        elif dealer_score == player_score:
                            print(f"Your final hand:{player_cards}, final score: {player_score}")
                            print(f"Computer's final hand:{dealer_cards}, final score: {dealer_score}")
                            print("You draw")
                            player_cards = []
                            player_score = 0
                            dealer_cards = []
                            dealer_score = 0
                            computer_turn = False
                            accept_play = False
                        else:
                            print(f"Your final hand:{player_cards}, final score: {player_score}")
                            print(f"Computer's final hand:{dealer_cards}, final score: {dealer_score}")
                            print("You win")
                            player_cards = []
                            player_score = 0
                            dealer_cards = []
                            dealer_score = 0
                            computer_turn = False
                            accept_play = False
