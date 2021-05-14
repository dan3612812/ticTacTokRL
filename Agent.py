import random
from copy import deepcopy
from env import EMPTY, NAMES, BOARD_FORMAT, DRAW
from lib import gameover,  emptystate


def enumStates(state, idx, agent):
    if idx > 8:
        player = 1 if idx % 2 == 0 else 2
        if player == agent.player:
            agent.add(state)
    else:
        winner = gameover(state)
        if winner != EMPTY:
            return
        for val in range(len(state)):
            state[idx] = val
            enumStates(state, idx+1, agent)


class Agent(object):
    def __init__(self, player, verbose=False, lossval=0, learning=True, explore=True):
        # self.values = {"attack": {}, "defensive": {}}
        self.values = {}
        self.player = player  # 1先攻 2後守
        self.verbose = verbose
        self.lossval = lossval
        self.learning = learning
        self.epsilon = 0.1
        self.alpha = 0.99
        self.prevstate = None
        self.prevScore = 0
        self.count = 0
        self.explore = explore
        enumStates(emptystate(), 0, self)

    def loadModel(self, values):
        self.values = values

    def episodeOver(self, winner):
        self.backup(self.reward(winner))
        self.prevstate = None
        self.prevScore = 0

    def action(self, oldState):
        state = deepcopy(oldState)
        r = random.random()
        if self.explore:
            if r < self.epsilon:
                move = self.random(state)
                self.log('====== Exploratory action: ' + str(move+1))
            else:
                move = self.greedy(state)
                self.log('====== Best action: ' + str(move+1))
        else:
            move = self.greedy(state)
            self.log('====== Best action: ' + str(move+1))
        state[move] = self.player
        self.prevstate = self.stateKey(state)
        self.prevScore = self.lookup(state)
        state[move] = EMPTY
        return move

    def random(self, state):
        available = []
        for i in range(len(state)):
            if state[i] == EMPTY:
                available.append(i)
        return random.choice(available)

    def greedy(self, state):
        maxval = -10
        maxmove = None
        if self.verbose:
            cells = []
        for i in range(len(state)):
            if(state[i] == EMPTY):
                state[i] = self.player
                val = self.lookup(state)
                state[i] = EMPTY
                if val > maxval:
                    maxval = val
                    maxmove = i
                if self.verbose:
                    cells.append('{0:.3f}'.format(val).center(6))
            elif self.verbose:
                cells.append(NAMES[state[i]].center(6))
        if self.verbose:
            print(BOARD_FORMAT.format(*cells))
        self.backup(maxval)
        return maxmove

    def backup(self, nextval):
        if self.prevstate != None and self.learning:
            self.whichValues()[self.prevstate] += self.alpha * \
                (nextval - self.prevScore)

    def whichValues(self):
        return self.values

    def lookup(self, state):
        key = self.stateKey(state)
        if not key in self.whichValues():
            self.add(key)
        return self.whichValues()[key]

    def add(self, state):
        winner = gameover(state)
        stateKey = self.stateKey(state)
        self.whichValues()[stateKey] = self.reward(winner)

    def reward(self, winner):
        if self.player == 1:
            # 先攻
            return self.rewardByFirst(winner)
        else:
            # 後守
            return self.rewardByLast(winner)

    def rewardByFirst(self, winner):
        # 先出手的當進攻方
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.2
        elif winner == DRAW:
            return 0
        else:
            return self.lossval

    def rewardByLast(self, winner):
        # 後出手的話 當防守方
        if winner == self.player:
            return 1
        elif winner == EMPTY:
            return 0.25
        elif winner == DRAW:
            return 0.5
        else:
            return self.lossval

    def outputModel(self):
        return self.values

    def stateKey(self, state):
        return "".join(str(e) for e in state)

    def log(self, s):
        if self.verbose:
            print(s)
