class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]] # new entry into the store
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            l = 0
            r = len(self.store[key]) - 1
            closest = ""
            while l <= r:
                mid = (l + r)//2
                if self.store[key][mid][1] <= timestamp:
                    closest = self.store[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return closest

            
