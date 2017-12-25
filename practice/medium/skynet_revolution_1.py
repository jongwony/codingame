import sys
from collections import deque

n, l, e = [int(i) for i in input().split()]
NODES = [tuple(int(j) for j in input().split()) for _ in range(l)]
GATEWAYS = [int(input()) for _ in range(e)]


class Problem:
    def __init__(self, root):
        self.root = root

    def next_depth(self, parent, node):
        a, b = node
        tmp = {a: b, b: a}
        return tmp.get(parent)

    def get_successors(self, parent):
        return {node for node in NODES if parent in node}

    def is_goal(self, parent):
        return parent in GATEWAYS

    def remove_node(self, a, b):
        if (a, b) in NODES:
            NODES.remove((a, b))
        elif (b, a) in NODES:
            NODES.remove((b, a))


class BFS:
    def __init__(self):
        self.open_set = deque()
        self.closed_set = set()
        self.meta = dict()

    def breath_first_search(self, problem):
        start = problem.root
        self.meta[start] = None
        self.open_set.append(start)

        while len(self.open_set) != 0:
            parent = self.open_set.popleft()

            if problem.is_goal(parent):
                return self.construct_path(parent)

            for node in problem.get_successors(parent):
                child = problem.next_depth(parent, node)
                if child in self.closed_set:
                    continue

                if child not in self.open_set:
                    self.meta[child] = parent
                    self.open_set.append(child)

            self.closed_set.add(parent)

    def construct_path(self, state):
        path = deque()
        current = state
        path.append(current)

        while True:
            row = self.meta.get(current)
            if row is not None:
                path.append(row)
                current = row
            else:
                break

        return path


while True:
    si = int(input())

    problem = Problem(si)
    bfs = BFS()

    exit, leaf, *_ = bfs.breath_first_search(problem)
    print(leaf, exit)
    problem.remove_node(leaf, exit)
