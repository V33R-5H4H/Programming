class conversion:
    def __init__(self):
        self.infix_expression=[]
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.postfix_expression = []
        self.prefix_expression = []
        self.operator_stack = []
        
    def infix_to_postfix(self,infix_expression):
        for char in infix_expression.split():
            if char.isalnum():
                self.postfix_expression.append(char)
            elif char == '(':
                self.operator_stack.append(char)
            elif char == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.postfix_expression.append(self.operator_stack.pop())
                self.operator_stack.pop()  # Remove the '('
            else:
                while (self.operator_stack and
                       self.operator_stack[-1] != '(' and
                       self.precedence[char] <= self.precedence[self.operator_stack[-1]]):
                    self.postfix_expression.append(self.operator_stack.pop())
                self.operator_stack.append(char)

        while self.operator_stack:
            self.postfix_expression.append(self.operator_stack.pop())

        return ' '.join(self.postfix_expression)
    
    def infix_to_prefix(self,infix_expression):
        for char in infix_expression.split()[::-1]:
            if char.isalnum():
                self.prefix_expression.append(char)
            elif char == ')':
                self.operator_stack.append(char)
            elif char == '(':
                while self.operator_stack and self.operator_stack[-1] != ')':
                    self.prefix_expression.append(self.operator_stack.pop())
                self.operator_stack.pop()
            else:
                while (self.operator_stack and
                       self.operator_stack[-1] != ')' and
                       self.precedence[char] <= self.precedence[self.operator_stack[-1]]):
                    self.prefix_expression.append(self.operator_stack.pop())
                self.operator_stack.append(char)

        while self.operator_stack:
            self.prefix_expression.append(self.operator_stack.pop())

        return ' '.join(self.prefix_expression[::-1])

inf=conversion()
print(inf.infix_to_postfix('A+B'))
