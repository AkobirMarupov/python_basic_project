#dfsfdsfadsfsdf
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo'sh!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bo'sh!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

steac = Stack()

steac.push(1)
steac.push(2)
steac.push(3)

print("Oxirgi element:", steac.peek())

print("Stackdagi elementlar soni:", steac.size())

print("Pop:", steac.pop())
print("Pop:", steac.pop())

print("Oxirgi element:", steac.peek())

print("Stack bo'shmi?", steac.is_empty())

