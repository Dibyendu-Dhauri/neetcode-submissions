class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []                    
        self.key_store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val = self.key_store.get(key,[])
        left,right = 0, len(val)-1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            if val[mid][1] <= timestamp:
                ans = val[mid][0]
                left += 1
            else:
                right -= 1
        return ans
