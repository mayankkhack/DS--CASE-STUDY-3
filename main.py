
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        current = self.top
        print("Stack:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.rear is None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def display(self):
        current = self.front
        print("Queue:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Popped:", stack.pop())
    stack.display()

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Dequeued:", queue.dequeue())
    queue.display()


if __name__ == "__main__":
    main()
