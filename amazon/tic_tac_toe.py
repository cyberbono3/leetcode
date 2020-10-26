
import collections
class TicTacToe(object):
    def __init__(self, n):
        self.dic = collections.defaultdict(int)
        def move(row, col, player):
            print("row", row, "col", col, "player", player)
            for i, x in enumerate((row, col, row+col, row-col)):
                self.dic[i, x, player] += 1
                print("i", i, "x", x, "player", player, "result",  self.dic[i, x, player])
                if self.dic[i, x, player] == n:
                    return player
            return 0
        self.move = move
t = TicTacToe(3)
t.move