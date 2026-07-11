class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self._build(arr, 2 * v, tl, tm)
            self._build(arr, 2 * v + 1, tm + 1, tr)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self._query(2 * v, tl, tm, l, min(r, tm)) + \
               self._query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(2 * v, tl, tm, pos, new_val)
            else:
                self._update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = self.tree[2 * v] + self.tree[2 * v + 1]