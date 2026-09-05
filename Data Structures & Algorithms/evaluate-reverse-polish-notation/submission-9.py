class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Evaluate each expression as we encounter it
        # We can use a stack to parse the tokens if we encounter a number we parse it to int and
        # put it on top of the stack.
        # If we encounter an operator, we pop the two operands off of the stack we can then apply the operator and add the result back to the stack

        stack = []

        for token in tokens:
            # print(stack)
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))

        return stack[-1]