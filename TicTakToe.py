from env import EMPTY, DRAW, BOARD_FORMAT, NAMES


class TieTakToe(object):
    def __init__(self):
        self.state = self.emptystate()
        self.playerName = NAMES
        self.idx = 0

    def action(self, number: int):
        """下一步棋:處理不能下的問題及判斷是否有贏家產生

        Args:
            number (int): 第幾格 0-8

        Raises:
            ValueError: 輸入number 範圍錯誤

        Returns:
            [type]: 參考 self.gameover()回傳
        """
        if(number > len(self.state) or self.state[number] != 0):
            print(self.state)
            raise ValueError("please put empty location i.e:1-9")
        self.state[number] = self.nowPlayerId()
        self.idx += 1
        return self.gameover()

    def nowPlayerId(self) -> int:
        return 1 if self.idx % 2 == 0 else 2

    def emptystate(self):
        """Description

        Returns:
            [int]: list
            default element is lib.EMPTY
        """
        return [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]

    def printBoard(self):
        """print now board
        Args:
            state ([int]): now board
        """
        cells = []
        for i in self.state:
            cells.append(self.playerName[i].center(6))
        print(BOARD_FORMAT.format(*cells))

    def gameover(self):
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
            if self.state[i] != EMPTY:
                count += 1
            if(self.state[a] != EMPTY and self.state[a] == self.state[b] and self.state[a] == self.state[c]):
                return self.state[a]

        if(count == 9):
            return DRAW
        else:
            return EMPTY
