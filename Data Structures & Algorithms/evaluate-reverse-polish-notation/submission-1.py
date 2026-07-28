from collections import deque

class Solution:
    def evalExpr(self, val1: int, val2: int, operator: str) -> int:
        match operator:
            case "+":
                return val1 + val2
            case "-":
                return val1 - val2
            case "*":
                return val1 * val2
            case "/":
                return int(val1 / val2)
            case _:
                return int('inf')

    def evalRPN(self, tokens: List[str]) -> int:
        # make a static list of operators to lookup for each stack value
        # keep adding values into stack until operator found
        # pop 2 recent values and perform operation
        # pop result back in
        # continue
        operators = {"+","-","*","/"}

        RPNStack = deque()

        for token in tokens:
            # case 1: operator found
            if token in operators:
                if len(RPNStack) >= 2:
                    val_2 = RPNStack.pop()
                    val_1 = RPNStack.pop()
                    RPNStack.append(self.evalExpr(int(val_1), int(val_2), token))
            else:
                RPNStack.append(token)

        return int(RPNStack[0])