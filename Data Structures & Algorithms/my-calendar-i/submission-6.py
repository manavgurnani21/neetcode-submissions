import bisect
from bisect import insort
from _bisect import bisect_left, bisect_right

class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        event = (startTime, endTime)
        if len(self.events) < 1:
            self.events.append(event)
            return True

        insert_idx = bisect.bisect(self.events, event)

        left_neighbor = insert_idx - 1
        right_neighbor = insert_idx

        left_skipped = left_neighbor < 0 or left_neighbor >= len(self.events)
        right_skipped = right_neighbor < 0 or right_neighbor >= len(self.events)

        if (left_skipped and not right_skipped) and (endTime <= self.events[right_neighbor][0]):
            insort(self.events, event)
            return True
        elif (not left_skipped and right_skipped) and (startTime >= self.events[left_neighbor][1]):
            insort(self.events, event)
            return True
        else:
            if startTime >= self.events[left_neighbor][1] and endTime <= self.events[right_neighbor][0]:
                insort(self.events, event)
                return True

        return False


# Your MyCalendar object will b, bisect_righte instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)