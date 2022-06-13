import random


def deal_card():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_chosen = random.choice(card_deck)
    return card_chosen


userCards = [deal_card(), deal_card()]
compCards = [deal_card(), deal_card()]
isGameOver = False

def compare_score(userScore, compScore):
    if userScore == compScore:
        return "ITS A DRAW !!!"
    elif compScore == 0:
        return "COMPUTER WON WITH A BLACKJACK !!!"
    elif userScore == 0:
        return "YOU WIN WITH A BLACKJACK !!!"
    elif userScore >21:
        return "YOU LOSE, YOUR SCORE WENT OVER 21"
    elif compScore > 21:
        return "YOU WIN, COMPUTER SCORE WENT OVER 21"
    elif userScore > compScore:
        return "YOU WIN !!!"
    else:
        return "YOU LOSE !!!"




def calc_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score>21:
        cards.remove(11)
        cards.append(1)
    return score


while not isGameOver:
    userScore = calc_score(userCards)
    compScore = calc_score(compCards)

    print(f"Your cards are {userCards} and score is {userScore}\nComputer first card is {compCards[0]}")

    if compScore == 0 or userScore > 21:
        isGameOver = True
        print("Computer Win !!!")
    elif userScore  == 0:
        isGameOver = True
        print("You Win :)")
    else:
        userChoice = input("Do You Want to Draw Another Card (y/n)")
        if userChoice in "yY":
            userCards.append(deal_card())
        else:
            isGameOver = True


while compScore != 0 and compScore <17:
    compCards.append(deal_card())
    compScore = calc_score(compCards)


print(compare_score(userScore,compScore))



