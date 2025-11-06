import random
from sys import flags


def build_standard_deck() -> list[dict]:
    Pack_of_cards = [
            {"rank": "2", "suite": "h"},
            {"rank": "2", "suite": "c"},
            {"rank": "2", "suite": "d"},
            {"rank": "2", "suite": "s"},
            {"rank": "3", "suite": "h"},
            {"rank": "3", "suite": "c"},
            {"rank": "3", "suite": "d"},
            {"rank": "3", "suite": "s"},
            {"rank": "4", "suite": "h"},
            {"rank": "4", "suite": "c"},
            {"rank": "4", "suite": "d"},
            {"rank": "4", "suite": "s"},
            {"rank": "5", "suite": "h"},
            {"rank": "5", "suite": "c"},
            {"rank": "5", "suite": "d"},
            {"rank": "5", "suite": "s"},
            {"rank": "6", "suite": "h"},
            {"rank": "6", "suite": "c"},
            {"rank": "6", "suite": "d"},
            {"rank": "6", "suite": "s"},
            {"rank": "7", "suite": "h"},
            {"rank": "7", "suite": "c"},
            {"rank": "7", "suite": "d"},
            {"rank": "7", "suite": "s"},
            {"rank": "8", "suite": "h"},
            {"rank": "8", "suite": "c"},
            {"rank": "8", "suite": "d"},
            {"rank": "8", "suite": "s"},
            {"rank": "9", "suite": "h"},
            {"rank": "9", "suite": "c"},
            {"rank": "9", "suite": "d"},
            {"rank": "9", "suite": "s"},
            {"rank": "10", "suite": "h"},
            {"rank": "10", "suite": "c"},
            {"rank": "10", "suite": "d"},
            {"rank": "10", "suite": "s"},
            {"rank": "J", "suite": "h"},
            {"rank": "J", "suite": "c"},
            {"rank": "J", "suite": "d"},
            {"rank": "J", "suite": "s"},
            {"rank": "Q", "suite": "h"},
            {"rank": "Q", "suite": "c"},
            {"rank": "Q", "suite": "d"},
            {"rank": "Q", "suite": "s"},
            {"rank": "K", "suite": "h"},
            {"rank": "K", "suite": "c"},
            {"rank": "K", "suite": "d"},
            {"rank": "K", "suite": "s"},
            {"rank": "A", "suite": "h"},
            {"rank": "A", "suite": "c"},
            {"rank": "A", "suite": "d"},
            {"rank": "A", "suite": "s"}
        ]
    return Pack_of_cards


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for x in range(swaps):
        i = random.randint(0,51)
        the_card = deck[i]
        flag = True
        while flag:
            j = random.randint(0,51)
            if j == i:
                continue
            else:
                if the_card["suite"] == "h" and j % 5 != 0 :
                    continue
                elif  the_card["suite"] == "c" and j % 3 != 0:
                    continue
                elif  the_card["suite"] == "d" and j % 2 != 0:
                    continue
                elif  the_card["suite"] == "s" and j % 7 != 0:
                    continue
                else:
                    deck[i],deck[j] = deck[j],deck[i]
                    flag = False
    return deck




# def card():
#     pack = []
#     num = [2, 3, 4, 5, 6, 7, 8, 9,10,"J","Q","K","A"]
#     type1 = ["h", "c", "d", "s"]
#     for i in num:
#         for y in type1:
#             type1 = ["h","c","d","s"]
#             dic = {"rank":str(i),"suite":y}
#             pack.append(dic)
#
#     return pack
#
# a = card()
# print(a)
































