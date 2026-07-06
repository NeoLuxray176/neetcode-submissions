class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lhs = int(tokens[0])
        rhs = int(tokens[1])

        for i in range(2,len(tokens)):
            token = tokens[i]

            print(f"{i} {lhs} {token} {rhs}")
            if token == '+':
                lhs = lhs + rhs
            elif token == '-':
                lhs = lhs - rhs
            elif token == '*':
                lhs = lhs * rhs
            elif token == '/':
                lhs = lhs // rhs
            else:
                rhs = int(tokens[i])

        return lhs
            
            
        