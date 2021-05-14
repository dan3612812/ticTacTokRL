from env import EMPTY, DRAW, NAMES

class Human(object):
    def __init__(self, player):
        self.player = player

    def action(self, state):
        # 處理輸入錯誤問題
        while True:
            action = input('which number do you move? range:1-9 : ')
            try:
                number = (int(action)-1)
                if(state[number] != EMPTY):
                    raise ValueError("is repeat")
                return number
                break
            except ValueError:
                print("please input empty location")
                pass
            except Exception:
                print("input error format")
                pass

    def episodeOver(self, winner):
        if winner == DRAW:
            print('Game over! It was a tie.')
        else:
            print('Game over! Winner: Player {0}'.format(NAMES[winner]))
