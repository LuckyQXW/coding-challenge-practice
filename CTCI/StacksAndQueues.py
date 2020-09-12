"""
Stack Min
Implement a stack which in addition to push and pop, also returns the min
element. All operations should be in O(1) time.
U:
push(1, 2, 3)
[1, 2, 3] -> min() = 1
push(-1)
[1, 2, 3, -1] -> min() = -1
pop()
[1, 2, 3] -> min() = 1

[] pop() -> illegal, returns None
[] min() -> illegal, returns None

M:
Use another stack to keep track of current min, pop as needed
Store current min in a tuple

P:
1. Use another stack
Pro: save a bit space since we don't need to store an extra min for every
     value pushed.
2. Store min in a tuple
[]
push() -> check for current min top[1], if None or val is smaller,
          set min to current val, if val is greater than curr min, maintain
          current min.
          push((val, min))
pop() -> empty, return None
min() -> empty, return None
push(1) -> [(1, 1)]
push() -> same
pop() -> pop the top node, update min to be the curr min on top. If empty,
         set to None
min() -> return top[1]
push(-1) -> [(1, 1), (-1, -1)]
Runtime: O(1) for all operations
Space: O(N) worst case
"""


class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val):
        curr_min = None
        if self.s:
            curr_min = min(self.s[-1][1], val)
        else:
            curr_min = val
        self.s.append((val, curr_min))

    def pop(self):
        if self.s:
            return self.s.pop()[0]
        else:
            return None

    def min(self):
        if self.s:
            return self.s[-1][1]
        else:
            return None


"""
R:
s = [(10, 10), (5, 5), (7, 5), (2, 2)]

push(10)
val = 10
curr_min = 10

push(5)
val = 5
curr_min = 5

push(7)
val = 7
curr_min = 5

push(2)
val = 2
curr_min = 2
min() = 2
pop() -> 2
"""

"""
Queue via Stacks
Implement a MyQueue class which implements a queue using two stacks
U:
Can only use two stacks, implement add(), remove(), peek(), and size()
M:
Use two stacks to simulate queue's FIFO nature
P:
Use a add_stack for every add operation, and another stack as to_remove.
When call remove(), if the to_remove stack is empty, transfer all elements
from add_stack to to_remove, and pop from the top of to_remove
"""


class MyQueue:
    def __init__(self):
        self.add_stack = []
        self.to_remove = []

    def add(self, val):
        self.add_stack.append(val)

    def remove(self):
        self.shift_stacks()
        if self.to_remove:
            return self.to_remove.pop()
        else:
            return None

    def peek(self):
        self.shift_stacks()
        if self.to_remove:
            return self.to_remove[-1]
        else:
            return None

    def size(self):
        return len(self.add_stack) + len(self.to_remove)

    def shift_stacks(self):
        if not self.to_remove:
            while self.add_stack:
                self.to_remove.append(self.add_stack.pop())
