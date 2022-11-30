import cards_test1

# Create the deck of cards

the_deck = cards_test1.Deck()
# the_deck.shuffle()

hand1 = []
hand2 = []
# while the_deck.is_empty() == False:
for i in range(5):
    card1 = the_deck.deal()
    hand1.append(card1)

    card2 = the_deck.deal()
    hand2.append(card2)

print("Starting Hands")
print("Hand1:", hand1)
print("Hand2:", hand2)
print()

keep_going = ''
while keep_going.lower() != 'n' and hand1 != [] and hand2 != []:
    battle_card1 = hand1[0].rank()
    battle_card2 = hand2[0].rank()
    if battle_card1 == 1:
        battle_card1 = 14
    if battle_card2 == 1:
        battle_card2 = 14
   
    if battle_card1 > battle_card2:
        print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(hand1[0],hand2[0]))
        Card_2 = hand2.pop(0)
        Card_1 = hand1.pop(0)

        hand1.append(Card_1)
        hand1.append(Card_2)
    elif battle_card1 < battle_card2:
        print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(hand1[0],hand2[0]))
        Card_2 = hand2.pop(0)
        Card_1 = hand1.pop(0)
       
        hand2.append(Card_2)
        hand2.append(Card_1)
    elif battle_card1 == battle_card2:
        print("Battle was 1: {}, 2: {}. Battle was a draw.".format(hand1[0],hand2[0]))
        Card_2 = hand2.pop(0)
        Card_1 = hand1.pop(0)
       
        hand2.append(Card_2)
        hand1.append(Card_1)

    print("hand1:", hand1)
    print("hand2:", hand2)
    if hand1 != [] and hand2 != []:
        print()
        keep_going = input("Keep Going: (Nn) to stop:")
   
   

if len(hand2)>len(hand1):
    print("Player 2 wins!!!")
elif len(hand1)>len(hand2):
    print("Player 1 wins!!!")
