class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Error: Stack is empty")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            print("Error: Stack is empty")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Part 1: Initial Operations from the Table
print("=== Part 1: Initial Operations ===")
S = Stack()

S.push(5)              # Stack: [5]
print(f"Operation: S.push(5) -> Stack: {S.items}")

S.push(3)              # Stack: [5, 3]
print(f"Operation: S.push(3) -> Stack: {S.items}")

print(f"Operation: len(S) -> Output: {len(S)}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

print(f"Operation: S.is_empty() -> Output: {S.is_empty()}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

print(f"Operation: S.is_empty() -> Output: {S.is_empty()}")

print(f"Operation: S.pop() -> Output: {S.pop()} (Error expected) -> Stack: {S.items}")

S.push(7)              # Stack: [7]
print(f"Operation: S.push(7) -> Stack: {S.items}")

S.push(9)              # Stack: [7, 9]
print(f"Operation: S.push(9) -> Stack: {S.items}")

print(f"Operation: S.top() -> Output: {S.top()}")

S.push(4)              # Stack: [7, 9, 4]
print(f"Operation: S.push(4) -> Stack: {S.items}")

print(f"Operation: len(S) -> Output: {len(S)}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

S.push(6)              # Stack: [7, 9, 6]
print(f"Operation: S.push(6) -> Stack: {S.items}")

S.push(8)              # Stack: [7, 9, 6, 8]
print(f"Operation: S.push(8) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

# Part 2: Additional Operations from the Second Sequence
print("\n=== Part 2: Additional Operations ===")
S = Stack()  # Start with a new empty stack

S.push(5)              # Stack: [5]
print(f"Operation: S.push(5) -> Stack: {S.items}")

S.push(3)              # Stack: [5, 3]
print(f"Operation: S.push(3) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

S.push(2)              # Stack: [5, 2]
print(f"Operation: S.push(2) -> Stack: {S.items}")

S.push(8)              # Stack: [5, 2, 8]
print(f"Operation: S.push(8) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

S.push(9)              # Stack: [5, 9]
print(f"Operation: S.push(9) -> Stack: {S.items}")

S.push(1)              # Stack: [5, 9, 1]
print(f"Operation: S.push(1) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

S.push(7)              # Stack: [5, 9, 7]
print(f"Operation: S.push(7) -> Stack: {S.items}")

S.push(6)              # Stack: [5, 9, 7, 6]
print(f"Operation: S.push(6) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

S.push(4)
print(f"Operation: S.push(4) -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")

print(f"Operation: S.pop() -> Output: {S.pop()} -> Stack: {S.items}")
