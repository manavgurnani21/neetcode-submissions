class MyCalendar:
    def __init__(self):
        self.events = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        # Approach:
        # go through events list
        #     if conflict exists, return False
        #     conflict defined by 4 cases:
        #         1. if current start falls between new start and end
        #         2. if current end falls between new start and end
        #         3. new start and end are in between current start and end
        #         4. new start before current start and new end after current end
        # otherwise, add the event and return true
        # print(f"booking for event: ({startTime}, {endTime})")

        for [eventStart, eventEnd] in self.events:
            # print(f"current start: {eventStart}, currentEnd: {eventEnd}")
            currStartOverlapOnly = startTime <= eventStart and endTime > eventStart
            # print("currStartOverlapOnly at", eventStart) if currStartOverlapOnly else 1
            currEndOverlapOnly = startTime < eventEnd and endTime >= eventEnd
            # print("currEndOverlapOnly at", eventEnd) if currEndOverlapOnly else 1
            completeInclusiveness = startTime >= eventStart and endTime <= eventEnd
            # print("completeInclusiveness") if completeInclusiveness else 1
            completeOverlap = startTime <= eventStart and endTime >= eventEnd
            # print("completeOverlap") if completeOverlap else 1
            if currStartOverlapOnly or currEndOverlapOnly or completeInclusiveness or completeOverlap:
                return False
            
        self.events.append([startTime, endTime])
        # print(self.events)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)