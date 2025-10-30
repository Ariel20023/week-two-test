from deck import *
from player_io import *
def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    for card in hand:
        if card["rank"] == "2" :
            hand_value += int(card["rank"])
        elif  card["rank"] == "3":
            hand_value += int(card["rank"])
        elif  card["rank"] == "4":
            hand_value += int(card["rank"])
        elif  card["rank"] == "5":
            hand_value += int(card["rank"])
        elif  card["rank"] == "6":
            hand_value += int(card["rank"])
        elif  card["rank"] == "7":
            hand_value += int(card["rank"])
        elif  card["rank"] == "8":
            hand_value += int(card["rank"])
        elif  card["rank"] == "9":
            hand_value += int(card["rank"])
        elif  card["rank"] == "10":
            hand_value += int(card["rank"])
        elif card["rank"] == "J" :
            hand_value += 10
        elif card["rank"] == "Q" :
            hand_value += 10
        elif card["rank"] == "K" :
            hand_value += 10
        else:
            hand_value += 1
    return int(hand_value)



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck[0])
    deck.pop(0)
    player["hand"].append(deck[0])
    deck.pop(0)
    dealer["hand"].append(deck[0])
    deck.pop(0)
    dealer["hand"].append(deck[0])
    deck.pop(0)
    print("The value of the player")
    print(calculate_hand_value(player["hand"]))
    print("The value of the dealer ")
    print(calculate_hand_value(dealer["hand"]))




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        dealer["hand"].append(deck[0])
        deck.pop(0)
    if calculate_hand_value(dealer["hand"]) > 21 :
        print("The player won")
        return False
    elif calculate_hand_value(dealer["hand"]) <= 21:
        return True






def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    while True:
        Player_decision = ask_player_action()
        if Player_decision == "H":
            player["hand"].append(deck[0])
            deck.pop(0)
            a_player_amount =calculate_hand_value(player["hand"])
            print(a_player_amount)
            if a_player_amount > 21:
                print("The player lost")
                calculation_of_player_value = calculate_hand_value(player["hand"])
                calculation_of_dealer_value = calculate_hand_value(dealer["hand"])
                print("The player's amount" + " " + str(calculation_of_player_value))
                print("The dealer's amount" + " " + str(calculation_of_dealer_value))
                break
        else:
            The_dealer_turn = dealer_play(deck,dealer)
            if The_dealer_turn:
                calculation_of_player_value = calculate_hand_value(player["hand"])
                calculation_of_dealer_value = calculate_hand_value(dealer["hand"])
                if calculation_of_player_value > calculation_of_dealer_value:
                    print("The player won")
                    print("The player's amount" +" "+str(calculation_of_player_value))
                    print("The dealer's amount" +" "+str(calculation_of_dealer_value) )
                    break
                elif calculation_of_player_value < calculation_of_dealer_value:
                    print("The dealer won")
                    print("The player's amount" +" "+str(calculation_of_player_value))
                    print("The dealer's amount" +" "+str(calculation_of_dealer_value))
                    break
                else:
                    print("draw")
                    print("The player's amount" +" "+str( calculation_of_player_value))
                    print("The dealer's amount" +" "+str(calculation_of_dealer_value))
                    break
            else:
                calculation_of_player_value = calculate_hand_value(player["hand"])
                calculation_of_dealer_value = calculate_hand_value(dealer["hand"])
                print("The player's amount" + " " + str(calculation_of_player_value))
                print("The dealer's amount" + " " + str(calculation_of_dealer_value))
                break












