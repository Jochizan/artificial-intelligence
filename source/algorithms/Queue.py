class Queue:

    def __init__(self):
        self.items = []

    def glue(self, x):
        self.items.append(x)

    def unglue(self):
        if self.is_empty():
            return 'La cola esta vacía'
        else:
            return self.items.pop(0)

    def is_empty(self):
        return self.items == []


queue = Queue()
print(queue.is_empty())
queue.glue(1)
print(queue.items)
queue.glue(2)
print(queue.items)
queue.glue(10)
print(queue.items)
queue.glue(10)
print(queue.items)
queue.glue(20)
print(queue.items)

queue.unglue()
print(queue.items)
queue.unglue()
print(queue.items)
queue.unglue()
print(queue.items)
queue.unglue()
print(queue.items)

print(queue.unglue())
print(queue.unglue())
print(queue.unglue())
print(queue.items)
