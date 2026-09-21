class Tree:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

    def insert(self, start, end):
        current = self
        while True:
            if start >= current.e:
                if not current.right:
                    current.right = Tree(start, end)
                    return True
                current = current.right
            elif end <= current.s:
                if not current.left:
                    current.left = Tree(start, end)
                    return True
                current = current.left
            else:
                return False


class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Tree(startTime, endTime)
            return True
        
        return self.root.insert(startTime, endTime)



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)