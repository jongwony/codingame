import sys
import math
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
cardp_1 = [input() for i in range(n)]

m = int(input())  # the number of cards for player 2
cardp_2 = [input() for i in range(m)]


class Card:
    RANK = [str(n) for n in range(2, 11)] + list('JQKA')

    def __init__(self, card):
        self.card = card

    def __repr__(self):
        return str(self.card)

    def __lt__(self, other):
        return self.RANK.index(self.card[:-1]) < self.RANK.index(other.card[:-1])

    def __gt__(self, other):
        return self.RANK.index(self.card[:-1]) > self.RANK.index(other.card[:-1])

    def __eq__(self, other):
        return self.RANK.index(self.card[:-1]) == self.RANK.index(other.card[:-1])


class Game:

    def __init__(self):
        self.player1 = deque(map(Card, cardp_1))
        self.player2 = deque(map(Card, cardp_2))
        self.p1_queue = deque()
        self.p2_queue = deque()
        self.count = 0
        self.winner = None

    def isend(self):
        if len(self.player1) == 0:
            self.winner = 2
            return False
        elif len(self.player2) == 0:
            self.winner = 1
            return False
        else:
            return True

    def main(self):
        while self.isend():
            p1 = self.player1.popleft()
            p2 = self.player2.popleft()
            self.p1_queue.append(p1)
            self.p2_queue.append(p2)

            self.fight(p1, p2)
            # print(self.player1, self.player2, file=sys.stderr)

        print(self.winner, self.count)

    def fight(self, p1, p2):
        if p1 == p2:
            self.war()
        else:
            [self.player2, self.player1][p1 > p2].extend(self.p1_queue + self.p2_queue)
            self.p1_queue, self.p2_queue = deque(), deque()
            self.count += 1

    def war(self):
        for _ in range(3):
            try:
                self.p1_queue.append(self.player1.popleft())
                self.p2_queue.append(self.player2.popleft())
            except IndexError:
                print('PAT')
                sys.exit(0)

        p1 = self.player1.popleft()
        p2 = self.player2.popleft()
        self.p1_queue.append(p1)
        self.p2_queue.append(p2)

        self.fight(p1, p2)


print(cardp_1, file=sys.stderr)
print(cardp_2, file=sys.stderr)
print(len(cardp_1), len(cardp_2), file=sys.stderr)

war_game = Game()
war_game.main()
