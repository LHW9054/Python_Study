def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("틱택토 게임을 시작합니다!")
    print_board(board)

    for _ in range(9):
        while True:
            try:
                row = int(input(f"{player} 플레이어, 행을 선택하세요 (0, 1, 2): "))
                col = int(input(f"{player} 플레이어, 열을 선택하세요 (0, 1, 2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("올바른 위치를 선택하세요.")
            except ValueError:
                print("올바른 숫자를 입력하세요.")

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"{player} 플레이어가 이겼습니다!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("무승부입니다!")

if __name__ == "__main__":
    tic_tac_toe()
