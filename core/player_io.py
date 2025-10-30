def ask_player_action() -> str:
    flage = True
    while flage:
        choice = str(input("If you want to continue, press H and if you want to stop, press S."))
        if choice.isalpha():
            if choice == "H" or choice == "S"  :
                flage = False
    return choice

print()