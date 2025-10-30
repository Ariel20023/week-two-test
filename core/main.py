from deck import *
from game_logic import *
if __name__ == "__main__":
    Pack_of_cards = build_standard_deck()
    Mixed_pack = shuffle_by_suit(Pack_of_cards)
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(Mixed_pack, player, dealer)


