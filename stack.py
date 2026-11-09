class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, data):
        self.top = Node(data, self.top)
        self.length += 1

    def peek(self):
        if self.top is None:
            raise IndexError("Стек порожній")
        return self.top.data

    def pop(self):
        data = self.peek()
        self.top = self.top.next
        self.length -= 1
        return data

    def clear(self):
        self.top = None
        self.length = 0

    def count(self):
        return self.length

    def size(self):
        return self.length

    def to_string(self):
        items = ["top"]
        node = self.top
        while node is not None:
            items.append(str(node.data))
            node = node.next
        items.append("null")
        return " -> ".join(items)

    def __str__(self):
        return self.to_string()


if __name__ == "__main__":
    stack = Stack()

    for value in (11, 22, 33):
        stack.push(value)
        print(f"push({value})  ->  {stack}")

    print("\npeek():", stack.peek())
    print("size():", stack.size())
    print("count():", stack.count())
    print("toString():", stack.to_string())

    print("\npop():", stack.pop())
    print("Після pop:", stack)
    print("size():", stack.size())

    stack.clear()
    print("\nПісля clear:", stack)
    print("size():", stack.size())

    try:
        stack.pop()
    except IndexError as error:
        print("pop() на порожньому стеку:", error)