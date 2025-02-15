class WiteText:
    def __init__(self):
        self.stack = []

    def write(self,value):
        self.stack.append(value)

    def ctr_z(self):
        return self.stack.pop()

    def display(self):
        return ' '.join(self.stack)


letter = WiteText()
letter.write('Hello')
letter.write(',')
letter.write(' ')
letter.write('Word')
letter.write('!')

print(letter.display())

print(letter.ctr_z())
print(letter.display())

