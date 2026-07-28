class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2:
            return [0]
        
        freqList = [0] * len(temperatures)
        freqStack = []
        freqStack.append(0)

        for i in range(1, len(temperatures)):
            while freqStack and temperatures[i] > temperatures[freqStack[-1]]:
                currIndex = freqStack.pop()
                freqList[currIndex] = i - currIndex
            freqStack.append(i)

        return freqList