# Names: Ibrahim Muamar, Alex Udvar, Amol Parmer
# Date: 21/1/2025
# File Name:
# Description: This is a game called The Big Seven which is an arcade simulator.

import random
import time


def intro_to_arcade():
    print("Welcome to Big Seven! At this arcade we have a variety of games to play such as Roulette and Blackjack with our own little spin on those classics. You will be given 100 tokens and make sure to have fun!")


def choose_game():
    time.sleep(1)
    print("1. Blackjack")
    print("2. Roulette")
    print("3. Rules")
    print("4. Quit")
    print("")

    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice <= 4 and user_choice >= 1:
                return user_choice
            else:
                print("Please enter a number between 1 and 4!")
        except:
            print("Please enter a valid integer!")


def bet_tokens(tokens):
    print("")
    time.sleep(1)
    while True:
        try:
            user_bet = int(input("How many tokens would you like to bet?: "))
            if user_bet > tokens:
                print("*You do not have enough tokens*")
            elif user_bet <= 0:
                print("Please input a positive number!")
            else:
                print("Your bet was: $" + str(user_bet))
                return user_bet
        except:
            print("Please input a valid number!")


def draw_card(tokens, ai_wins, user_bet):
    user_cards = []
    ai_cards = []
    cardslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_card1 = random.choice(cardslist)
    user_card2 = random.choice(cardslist)

    time.sleep(1)
    print("")
    print("Dealer: Good luck, I'm a well-known man in this arcade!")

    user_cards.append(user_card1)
    user_cards.append(user_card2)

    time.sleep(1)

    if user_card1 == 7 and user_card2 == 7:
        print("*You drew 2 7's congratulations you won!*")
        tokens = tokens + user_bet * 2
        time.sleep(1)
        return user_cards, ai_cards, tokens, True

    ai_card1 = random.choice(cardslist)
    ai_card2 = random.choice(cardslist)

    ai_cards.append(ai_card1)
    ai_cards.append(ai_card2)

    time.sleep(1)

    if ai_card1 == 7 and ai_card2 == 7:
        print("Dealer: HAHA. I win! Good luck next time")
        time.sleep(0.5)
        print("*The Dealer drew 2 7's, You lose!*")
        ai_wins = ai_wins + 1
        tokens = tokens - user_bet
        time.sleep(1)
        return user_cards, ai_cards, tokens, False

    if user_card1 == 2 or user_card2 == 2:
        print("*You drew '2'. You and the Dealer will draw an extra card.*")
        user_cards.append(2)
        ai_cards.append(2)
        time.sleep(1)

    print("*Your initial deck: " + str(user_cards) + "*")
    time.sleep(1)
    print("*Dealer initial deck: " + str(ai_cards) + "*")
    print("")
    time.sleep(1)

    return user_cards, ai_cards, tokens, None


def hit_or_stay(user_cards, ai_cards, tokens, user_bet):
    user_cards_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "?"]
    ai_cards_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    mystery_values = []

    while True:
        try:
            user_choice = input("Would you like to Hit or Stay: ").lower()

            if user_choice == "hit":
                new_card = random.choice(user_cards_list)

                if new_card == "?":
                    mystery_value = random.randint(1, 10)
                    mystery_values.append(mystery_value)
                    user_cards.append("?")
                    print("*You drew a mystery card!*")
                    time.sleep(1)
                else:
                    user_cards.append(new_card)
                    print("You drew a " + str(new_card) + "*")

                print("")
                print("*Your hand: " + str(user_cards) + "*")

                if user_cards.count(7) == 2:
                    print("Lucky 7! You have two 7's in your hand. You win!!")
                    tokens = tokens + user_bet * 2
                    return tokens, True

                total = 0
                for card in user_cards:
                    if card != "?":
                        total += card

                total += sum(mystery_values)

                if total > 21:
                    print("*You went bust! Your total is " + str(total) + "*")
                    tokens = tokens - user_bet
                    return tokens, False

            elif user_choice == "stay":
                print("*You chose to stay. Revealing your hand...*")
                time.sleep(1)

                for i in range(len(user_cards)):
                    if user_cards[i] == "?":
                        user_cards[i] = mystery_values[0]
                        del mystery_values[0]

                print("*Your final hand: " + str(user_cards) + "*")
                user_total = sum(user_cards)

                time.sleep(1)
                print("Dealer's turn to draw cards...")
                time.sleep(1)

                while sum(ai_cards) < 17:
                    ai_card = random.choice(ai_cards_list)
                    ai_cards.append(ai_card)
                    print("*AI drew a " + str(ai_card) + "*")
                    time.sleep(1)

                print("")
                print("*AI's final hand: " + str(ai_cards) + "*")

                ai_total = sum(ai_cards)

                time.sleep(1)

                if ai_total > 21 or user_total > ai_total:
                    print("Congratulations, you win!")
                    tokens = tokens + user_bet * 2
                    return tokens, True
                elif user_total == ai_total:
                    print("It's a tie! Your bet is returned.")
                    return tokens, None
                else:
                    print("AI wins! Better luck next time.")
                    tokens = tokens - user_bet
                    return tokens, False

            else:
                print("Please enter either Hit or Stay.")
                print("")

        except:
            print("Invalid Input!")
            print("")


def blackjack(tokens, ai_wins):
    user_bet = bet_tokens(tokens)

    user_cards, ai_cards, tokens, game_status = draw_card(tokens, ai_wins, user_bet)

    if game_status is None:
        tokens, game_status = hit_or_stay(user_cards, ai_cards, tokens, user_bet)

    time.sleep(1)

    if game_status == False:
        print("You lost! Maybe get better at the game!")
    elif game_status:
        print("You won! Maybe you're actually good")
    else:
        print("You had a tie! No tokens were won or lost.")

    print("")
    print("Your new total tokens: " + str(tokens))

    return tokens


def number_colour():
    numbers = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26,
        27, 28, 29, 30, 31, 32, 33, 34,
        35, 36
    ]

    lucky_colour = random.choice(["red", "black", "white", "green"])

    print("Lucky color for this round is:", lucky_colour)
    print("")

    colour_red = []
    colour_black = []
    colour_green = []
    colour_white = []

    if lucky_colour != "red":
        for x in range(10):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_red.append(number_generated)
    else:
        for x in range(6):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_red.append(number_generated)

    if lucky_colour != "black":
        for x in range(10):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_black.append(number_generated)
    else:
        for x in range(6):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_black.append(number_generated)

    if lucky_colour != "white":
        for x in range(10):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_white.append(number_generated)
    else:
        for x in range(6):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_white.append(number_generated)

    if lucky_colour != "green":
        for x in range(10):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_green.append(number_generated)
    else:
        for x in range(6):
            number_generated = random.choice(numbers)
            numbers.remove(number_generated)
            colour_green.append(number_generated)

    return colour_red, colour_black, colour_white, colour_green


def display_board(board):
    print("Roulette Board:")

    for color, numbers in board:
        print(color.capitalize() + ": " + str(sorted(numbers)))


def roulette(tokens):
    red_numbers, black_numbers, white_numbers, green_numbers = number_colour()

    board = []
    colors = ["red", "black", "white", "green"]

    tokens_starting = tokens

    for color in colors:
        if color == "red":
            board.append(["red", red_numbers])
        elif color == "black":
            board.append(["black", black_numbers])
        elif color == "white":
            board.append(["white", white_numbers])
        elif color == "green":
            board.append(["green", green_numbers])

    display_board(board)

    bet_value = bet_tokens(tokens)

    bet_type = input("Enter your bet type (color, number, even, odd, zero): ").lower()

    bet_number = 0
    bet_color = ""

    if bet_type == "number":
        bet_value = int(bet_value)
        bet_number = int(input("Enter the number you want to bet on (0-36): "))
    elif bet_type == "color":
        bet_color = input("Enter the color you want to bet on (red, black, white, green): ").lower()

    all_numbers = []

    for numbers in [red_numbers, black_numbers, white_numbers, green_numbers]:
        all_numbers += numbers

    winning_number = random.choice(all_numbers)

    if winning_number in red_numbers:
        winning_color = "red"
    elif winning_number in black_numbers:
        winning_color = "black"
    elif winning_number in white_numbers:
        winning_color = "white"
    else:
        winning_color = "green"

    print("Winning number:", winning_number, "Winning color:", winning_color)

    if bet_type == "number" and bet_number == winning_number:
        tokens += bet_value * 36
    elif bet_type == "color" and bet_color == winning_color:
        tokens += bet_value * 2
    elif bet_type == "even" and winning_number % 2 == 0 and winning_number != 0:
        tokens += bet_value * 2
    elif bet_type == "odd" and winning_number % 2 != 0:
        tokens += bet_value * 2
    elif bet_type == "zero" and winning_number == 0:
        tokens += bet_value * 36
    else:
        tokens -= bet_value

    if tokens > tokens_starting:
        print("Congratulations! You won! Your new token balance is:", tokens)
    else:
        print("You lost! Your new token balance is:", tokens)

    return tokens


def display_rules():
    print("1. BlackJack Rules")
    print("2. Roulette Rules")
    print("3. How do Tokens Work?")

    while True:
        try:
            rules_choice = int(input("Enter your choice: "))

            if rules_choice < 1 or rules_choice > 3:
                print("Please choose an option above")
                print("")
            else:
                break

        except:
            print("Please enter a valid integer!")
            print("")

    if rules_choice == 1:
        time.sleep(1)
        print("Blackjack is trying to build a hand of cards that total to as close to 21 as possible. All kings, queens and jacks are worth 10. If your hand is > 21, you go bust and lose. You have a choice to hit (draw) or stay (keep). If you draw a 2 in your initial hand, the dealer gets a 2. Two 7's in your hand mean you win via Lucky Seven. There is also a mystery card whose value is unknown until the end of the round.")
        print("")

    elif rules_choice == 2:
        time.sleep(1)
        print("In the Roulette game, you place a bet on one of several options: color (red, black, white, green), a specific number (0-36), or other bet types like even, odd, or zero. To play, first decide how many tokens you'd like to bet. Then choose your bet type and enter the amount you'd like to wager. The game will randomly select a winning number and color from the roulette wheel. If your bet matches the result, you win tokens based on the bet type: betting on a number wins you 36 times your bet, betting on a color or even/odd wins you 2 times your bet, and betting on zero wins you 36 times your bet. If you lose, you lose the amount of your bet. The game continues as long as you have tokens to wager.")
        print("")

    else:
        time.sleep(1)
        print("The tokens you start with is 100. There are different odds for each game and if you reach 0. You lose! Have fun!")


def main():
    tokens = 100
    ai_wins = 0

    intro_to_arcade()

    while True:
        print("You have " + str(tokens) + " tokens.")

        choice = choose_game()

        if choice == 1:
            time.sleep(1)
            tokens = blackjack(tokens, ai_wins)

        elif choice == 2:
            time.sleep(1)
            tokens = roulette(tokens)

        elif choice == 3:
            time.sleep(1)
            display_rules()
            continue

        else:
            print("Thanks for visiting the Big Seven Arcade! See you again!")
            break

        if tokens <= 0:
            time.sleep(1)
            print("You've run out of tokens, the game is over!")
            print("")
            print("Thanks for visiting the Big Seven Arcade!")
            break

        time.sleep(2)

        play_again = input("Write 'yes' to play again, 'no' otherwise: ").lower()

        if play_again == "no":
            print("Thanks for visiting the Big Seven Arcade! See you again!")
            break


main()
