import matplotlib.pyplot as plt
from env import EMPTY,  DRAW


def emptystate():
    """Description

    Returns:
        [int]: list
        default element is lib.EMPTY
    """
    return [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]


def gameover(state):
    """check board to judgment who is winner
    Args:
        state ([int]):board

    Returns:
        Int: winner value or lib.DRAW
    """
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    count = 0
    for i in range(len(lines)):
        a, b, c = lines[i]
        if state[i] != EMPTY:
            count += 1
        if(state[a] != EMPTY and state[a] == state[b] and state[a] == state[c]):
            return state[a]

    if(count == 9):
        return DRAW
    else:
        return EMPTY


def play(agent1, agent2):
    """start game

    Args:
        agent1 (Agent): playerA
        agent2 (Agent): playerB

    Returns:
        Int: which player winner
    """
    state = emptystate()
    # 最多9步
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return DRAW


def plotPicture(playCount: int, profA1win: list, profA2win: list, profdraw: list, fileName="vs.png"):

    plt.plot(list(range(0, playCount)), profA1win, label="A win", color='r')
    plt.plot(list(range(0, playCount)), profA2win, label="B win", color='b')
    plt.plot(list(range(0, playCount)), profdraw, label="tie", color='g')
    plt.ylabel("count")
    plt.xlabel("round")
    plt.legend()
    plt.savefig(fileName, bbox_inches='tight')
    plt.show()
