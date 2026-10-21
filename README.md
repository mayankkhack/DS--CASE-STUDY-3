# Case Study 3: Stack and Queue Using Linked Lists

## Unit III: Linked Lists

**Subject:** Data Structures and Algorithms  
**Language:** Python 3

## Aim
To implement Stack and Queue data structures using linked lists.

## Objectives
- Perform push and pop operations on a Stack.
- Perform enqueue and dequeue operations on a Queue.
- Understand node-based dynamic memory representation.

## Theory

A linked list consists of nodes containing data and a reference to the next node.

**Stack:** Follows LIFO (Last In, First Out). Insertion and deletion take place at the top.

**Queue:** Follows FIFO (First In, First Out). Insertion takes place at the rear and deletion takes place at the front.

## Operations
- Stack: Push, Pop, Display.
- Queue: Enqueue, Dequeue, Display.

## Sample Output

```text
Stack: 30 20 10
Popped: 30
Stack: 20 10
Queue: 10 20 30
Dequeued: 10
Queue: 20 30
```

## Complexity
- Stack push and pop: `O(1)`
- Queue enqueue and dequeue: `O(1)`
- Display: `O(n)`

## Applications
- Stack: Function calls, undo operations, expression evaluation.
- Queue: Task scheduling, printer queues, request processing.

## How to Run
```bash
python main.py
```

## Conclusion
Linked lists provide a dynamic way to implement Stack and Queue without requiring a fixed-size array.
