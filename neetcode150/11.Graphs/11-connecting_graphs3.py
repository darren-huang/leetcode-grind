"""took 8 minutes, passes with just 1 bug (inputs were 1 indexed instead of 0 indexed)

"""


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """

    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [1] * n
        self.num_components = n

    def _get_root(self, i):
        orig = i
        while self.parent[i] != i:
            i = self.parent[i]
        self.parent[orig] = i
        return i

    def connect(self, a, b):
        a, b = a - 1, b - 1
        ra, rb = self._get_root(a), self._get_root(b)
        if ra != rb:
            # if not equal then connect
            if self.weight[ra] < self.weight[rb]:
                ra, rb = rb, ra  # makes ra bigger weight
            self.parent[rb] = ra  # small points to bigger
            self.weight[ra] += self.weight[rb]  # update wieght
            self.num_components -= 1

    """
    @return: An integer
    """

    def query(self):
        return self.num_components
