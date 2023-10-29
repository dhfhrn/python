def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        answer.append(temp)
    x = 0
    y = 0

    for i in range(n*n):
        answer [x][y] = n+1






    return answer

def display_board(board):
    for i in range(3):
        print("-------------")
        print(f"| {board[3*i]} | {board[3*i+2]} | {board[3*i+2]} |")
    print("-------------")

def input_OX():
    print("O나 X 중에서 선택하세요:")
    while True:
        a = input()
        if a == 'O':
            b = 'X'
            return a, b
        elif a == 'X':
            b = 'O'
            return a, b
        else:
            print('다른 문자를 선택해주세요')

    # O나 X 중에서 선택해주세요: O, X
    # 사용자가 O나 X를 입력한다. 만일 O나 X가 아닌 다른 문장이 들어오면 다시 입력 받는다.
    # O가 입력되면 컴퓨터는 자동으로 X, X가 입력되면 컴퓨터는 O
    # 입력받은 문양의 반대되는 문양을 컴퓨터 문양으로 지정한다
    # 사용자문양, 컴퓨터문양 순으로 return한다


def input_POS():

    # 사용자가 문양을 놓을 위치를 입력받는다.(1~9)
    # 입력받은 자리가 놓아도 되는 자리인지 판단한다
    # 만약 입력한 자리가 올바르지 않은 자리라면 다시 입력받는다
    # 제대로 입력받았다면 해당 자리를 return한다
    return

def VICTORY():
    # 유저가 우승했을 경우 Ture, 아닌경우 False를 return한다
    # 우승 조건은 한 줄 빙고로, 가로3, 세로3, 대각선2개의 경우가 있다
    return

def random_POS():
    # 랜덤한 정수를 만들어 커퓨터의 문양을 넣을 좌표로 본다
    # 만약 올바른 좌표가 아니라면 다시 만든다.
    # 잘 만들어 졌다면 return 한다
    return

if __name__ == "__main__":
    board = ['*'] * 9
    display_board(board)
    player, computer = input_OX()
    print(player, computer)

# 틱텍토
# 게임 실행 과정
# 보드판 준비(1차원 리스트)
# o, x 고르기(컴퓨터의 문양은 반대 문장으로 설정) <- inputOX()
# 보드판 출력--------------------------------------------
# 사용자 자리 입력(입력받은 자리가 올바른 자리인지 확인) <- inputPOS()
# 보드판 출력--------------------------------------------
# 우승조건 확인 <- victory()
# 우승조건 성립하면, 플레이어 승 촐력 후 게임 종료
# 컴퓨터 입력(랜덤한 정수를 만들어서 해당 자리에 컴퓨터 문양 삽입)
# 보드판 출력---------------------------------------------
# 컴퓨터가 우승인지 확인 <- victory()
# 컴퓨터가 우승조건에 성립하면 컴퓨터승 출력후, 게임 종료
# 보드판에 넣을 공간이 없을 때 까지 3~8까지 반복

--------------------------------------------------------------------------------------------------------------------------------------------------

from tictactoe_func import*

board = ['*'] * 9

player, computer = input_OX()

display_board(board)

while True:
    pos = input_POS()
    board[pos] = player

    display_board(board)

    if VICTORY():
        print("player win!")
        exit()

    pos = random_POS()
    board[pos] = computer

    display_board(board)

    if VICTORY():
        print("computer win!")
        exit()
