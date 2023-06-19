piece_composer = {}
piece_key = {}

n = int(input())

for _ in range(n):
    command = input()
    command_args = command.split("|")
    piece = command_args[0]
    composer = command_args[1]
    key = command_args[2]
    
    piece_composer[piece] = composer
    piece_key[piece] = key
    
while True:
    line = input()
    if line == "Stop":
        break
    
    line_args = line.split("|")
    action = line_args[0]
    piece = line_args[1]
    if action == "Add":
        composer = line_args[2]
        key = line_args[3]
        
        if piece not in piece_composer:
            piece_composer[piece] = composer
            piece_key[piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        if piece in piece_composer:
            piece_composer.pop(piece)
            piece_key.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        new_key = line_args[2]
        if piece in piece_key:
            piece_key[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            
sorted_pieces = dict(sorted(piece_composer.items(), key = lambda x: (x[0], x[1])))
            
for piece, composer in sorted_pieces.items():
    print(f"{piece} -> Composer: {composer}, Key: {piece_key[piece]}")