class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if len(s) < 2:
            return False
        p_stack = deque([])
        for c in s:
            if c == '(':
                p_stack.appendleft(')')
            elif c == '{':
                p_stack.appendleft('}')
            elif c == '[':
                p_stack.appendleft(']')
            else:
                if len(p_stack) == 0 or c != p_stack[0]:
                    return False
                p_stack.popleft()

        return len(p_stack) == 0