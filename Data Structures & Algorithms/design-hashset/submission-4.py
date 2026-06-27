class MyHashSet:

    def __init__(self):
        self.container = []

    def add(self, key: int) -> None:
        if key not in self.container:
            self.container.append(key)

    def remove(self, key: int) -> None:
        if key in self.container:
            self.container.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.container:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)