class FreqStack:

    def __init__(self):
        self.cnt = {} # here we store the cnt of each element like {5:3, 7:2, 4:1}
        self.max_cnt = 0 # here we maintain the maximum count among the all element
        self.stack = {} # here we store the cnt along with elements the format we store like
        # {
            # 1:[5,7,4],
            # 2:[5,7],
            # 3:[5]
            # } 
            # we store this way , so we can also maintain the order of peak element when the max_cnt is same

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