from typing import List


class stack_obj:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []
        return self.stack

    # def __str__(self):
    #     return str(self.stack)

    # def __repr__(self):
    #     return str(self.stack)

