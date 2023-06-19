def get_char_result (half, char):
    counter = 0
    for ch in half:
        if ch == char:
            counter += 1
    return counter >= 6 and counter < 10

tickets = [ticket.strip for ticket in input().split(", ")]

symbols = ["@", "#", "$", "^"]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    
    left_part = ticket[:10]
    right_part = ticket[10:]
    
    for symbol in ticket:
        get_char_result()