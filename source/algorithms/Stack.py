class Stack:

    def __init__(self):
        self.items = []

    def glue(self, x):
        self.items.append(x)

    def unglue(self):
        if self.is_empty():
            return 'La pila esta vacía'
        else:
            return self.items.pop()

    def is_empty(self):
        return self.items == []


stack = Stack()
print(stack.is_empty())
stack.glue(1)
print(stack.items)
stack.glue(2)
print(stack.items)
stack.glue(10)
print(stack.items)
stack.glue(10)
print(stack.items)
stack.glue(20)
print(stack.items)

stack.unglue()
print(stack.items)
stack.unglue()
print(stack.items)
stack.unglue()
print(stack.items)
stack.unglue()
print(stack.items)

print(stack.unglue())
print(stack.unglue())
print(stack.unglue())
print(stack.items)
