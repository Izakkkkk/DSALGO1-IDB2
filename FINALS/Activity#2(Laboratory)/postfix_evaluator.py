class postfix_evaluator:
    def __init__(self):
        self.stack = []

    def evaluate(self, expression):
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                right = self.stack.pop()
                left = self.stack.pop()
                result = self.apply_operator(left, right, token)
                self.stack.append(result)

            return self.stack.pop()

        def apply_operator(self, left, right, operator):
            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right
            elif operator == "/":
                return left / right
            else:
                raise ValueError("Unknown Operator: {operator}")


if __name__ == '__main__':
    evaluator = postfix_evaluator()
    print("Enter a Postfix Expression: ")
    user_input = input().strip()
    try:
        result = evaluator.evaluate(user_input)
        print(f"Result of the Postfix Expression: {result}")
    except Exception as e:
        print(f"Error: {e}")