def print_board(b):
    for r in b:
        print(" | ".join(r))
        print("-" * 9)

def check_winner(b):
    for r in b:
        if r[0] == r[1] == r[2] != " ": return r[0]
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] != " ": return b[0][c]
    if b[0][0] == b[1][1] == b[2][2] != " ": return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != " ": return b[0][2]
    return None

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    print("Game loaded. Player X vs AI O.")

if __name__ == "__main__":
    main()
