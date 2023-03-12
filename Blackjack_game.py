import random


def cards_score(list_of_cards):
    sum = 0
    for card in list_of_cards:
        sum = card + sum
    return sum


def dealers_score(list_of_cards):
    sum = 0
    for card in list_of_cards:
        sum = card + sum
    return sum


print("Welcome to my Blackjack game!")

player_name = input("What is your name?\n")

print(player_name,"welcome to Blackjack. To win, get as close to 21 as possible without going over! If you go over 21 you lose.")


hit = "hit"
stick = "stick"

cards = []
cards.append(random.randint(1, 11))
cards.append(random.randint(1, 11))

#dealers_score = dealers_hand
#
# while dealers_score(cards) <= 17:
#     new_card = random.randint(1, 11)
#    # dealers_score = append.new_cards)
#     print(dealers_score)
#     if dealers_score(cards) + new_card >= 17:
#         if dealers_score(cards) + new_card <= 21:
#             print(dealers_score)
#             break
#     else:
#         print(dealers_score)


print(f"Your a hand is,{cards}")


while cards_score(cards) < 21:
    print("Would you like to) stick or hit (? ")
    user_input = input()
    if user_input == hit:

        new_card = random.randint(1, 11)
        print(new_card)
        cards.append(new_card)
        print(cards)
        total_new_cards = cards_score(cards)
        print(total_new_cards)


    if user_input == stick:
        print("You have chosen to stick. Lets see what the dealer has!")
        if cards_score > dealers_score:
            print("Congratulations! You had the winning hand!")
        break

if cards_score(cards) > 21:
    print("Bust!")
if cards_score(cards) == 21:
    print("Winner Winner Chicken Dinner!!")

final_score = cards_score(cards)

    #while:
     #   dealers_hand (<= 17)
      #  ("hit")
       # print(card_score)
    #if:
     #   dealers_hand (>17 and <=21)
      #  ("stick")
       # print(card_score)




#break

    #else(cards + cards) <= 21:
#print("Bust!")


#input()



#for.
     # card1 > < 11 = "Ace"
     # card2 = 2
     # card3 = 3
     # card4 = 4
     # card5 = 5
     # card6 = 6
     # card7 = 7
     # card8 = 8
     # card9 = 9
     #    10 = "Jack", "Queen", "King"
     #11 = "Ace"


