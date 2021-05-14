import pickle
from Agent import Agent
from lib import play,  DRAW


def train(count: int):
    agent1 = Agent(1, lossval=-1)
    agent2 = Agent(2, lossval=-1)
    countA1Win = 0
    countA2Win = 0
    countDraw = 0
    profA1win = []
    profA2win = []
    profdraw = []
    for i in range(count):
        if i % 10 == 0:
            print('Game: {0}'.format(i))

        winner = play(agent1, agent2)
        agent1.episodeOver(winner)
        agent2.episodeOver(winner)
        if winner == DRAW:
            countDraw += 1
        elif winner == 1:
            countA1Win += 1
        else:
            countA2Win += 1

        profA1win.append(countA1Win)
        profA2win.append(countA2Win)
        profdraw.append(countDraw)

    # 輸出攻擊model
    with open("self-A.pickle", "wb")as f:
        pickle.dump(agent1.outputModel(), f)
    # 輸出防守model
    with open("self-D.pickle", "wb")as f2:
        pickle.dump(agent2.outputModel(), f2)

def main():
    train(100000)

if __name__ == "__main__":
    main()
