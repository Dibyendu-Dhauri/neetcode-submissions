class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0
        self.stack = {}

    def push(self, val: int) -> None:
        self.cnt[val] = self.cnt.get(val,0) + 1
        val_cnt = self.cnt[val]
        if val_cnt > self.max_cnt:
            self.max_cnt = val_cnt
            self.stack[val_cnt] = []
        self.stack[val_cnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_cnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.max_cnt]:
            self.max_cnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()