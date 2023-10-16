import random

def init_board():
    board = [[' ' for _ in range(5)] for _ in range(5)]
    return board

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 17)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(5):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(5)) or all(board[i][4 - i] == player for i in range(5)):
        return True

    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = init_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    
    print("틱택톡 게임을 시작합니다!\n")
    
    for _ in range(25):
        print_board(board)
        print(f"현재 차례: {current_player}\n")
        
        while True:
            row = int(input("행을 선택하세요 (1-5): ") - 1)
            col = int(input("열을 선택하세요 (1-5): ") - 1)
            if 0 <= row < 5 and 0 <= col < 5 and board[row][col] == ' ':
                break
            else:
                print("유효하지 않은 위치입니다. 다시 시도하세요.")

        board[row][col] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player}가 이겼습니다! 축하합니다!")
            break
        elif is_full(board):
            print_board(board)
            print("무승부입니다!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    play_game()
