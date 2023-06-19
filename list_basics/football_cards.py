input_line = input()
cards_list = input_line.split()

cards_first_team = []
cards_second_team = []

total_players = 11
isTerminated = False
for card in cards_list:
    card_args = card.split("-")
    card_team = card_args[0]
    
    if card_team == "A":
        cards_first_team.append(card_args[1])
    else:
        cards_second_team.append(card_args[1])
        
    if len(set(cards_first_team)) > 4 or len(set(cards_second_team)) > 4:
        isTerminated = True
        break
        
print(f"Team A - {total_players - len(set(cards_first_team))}; Team B - {total_players - len(set(cards_second_team))}")

if isTerminated:
    print("Game was terminated")