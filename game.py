from env import DRAW, EMPTY
import pickle
from Agent import Agent
from Human import Human
from TicTakToe import TieTakToe

attackModelFile = "model-A.pickle"  # change your first player model weight
defendModelFile = "model-D.pickle"  # change your last player model weight


def main():
    # 初始化
    roundCount = 0
    attackAgent = Agent(1, True, -1, explore=False)
    defendAgent = Agent(2, True, -1, explore=False)
    # 載入 兩個model
    with open(attackModelFile, "rb") as modelA:
        data = pickle.load(modelA)
        attackAgent.loadModel(data)

    with open(defendModelFile, "rb")as modelD:
        data = pickle.load(modelD)
        defendAgent.loadModel(data)

    # 初始化玩家遊戲介面
    human = Human(1)
    # 遊戲開始
    while True:
        roundCount += 1
        print("round {}".format(str(roundCount)))
        if roundCount % 2 == 0:
            winner = play(attackAgent, human)
            attackAgent.episodeOver(winner)
        else:
            winner = play(human, defendAgent)
            defendAgent.episodeOver(winner)

        human.episodeOver(winner)


def play(playerA, playerB):
    """start game

    Args:
        playerA : playerA
        PlayerB : playerB

    Returns:
        Int: which player winner
    """
    board = TieTakToe()
    board.printBoard()
    for i in range(9):
        if i % 2 == 0:
            move = playerA.action(board.state)
        else:
            move = playerB.action(board.state)
        winner = board.action(move)
        board.printBoard()
        if winner != EMPTY:
            board.printBoard()
            return winner
    return DRAW


if __name__ == "__main__":
    main()
