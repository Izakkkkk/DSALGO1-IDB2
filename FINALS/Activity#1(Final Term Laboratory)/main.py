from LinkedDeque import LinkedDeque as Deque
from LinkedQueue import LinkedQueue as Queue
from LinkedStack import LinkedStack as Stack


D = Deque()
Q = Queue()
S = Stack()


D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(5)
D.insert_last(4)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)


Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())


Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())


while not D.is_empty():
    Q.enqueue(D.delete_first())


print("Deque D after reordering using Queue:")
while not Q.is_empty():
    D.insert_last(Q.dequeue())


for element in D:
    print(element)


D = Deque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(5)
D.insert_last(4)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)


S.push(D.delete_first())
S.push(D.delete_first())
S.push(D.delete_first())


S.push(D.delete_first())
S.push(D.delete_first())


while not D.is_empty():
    S.push(D.delete_first())


D.insert_first(S.pop())
D.insert_first(S.pop())


while not S.is_empty():
    D.insert_first(S.pop())


print("Deque D after reordering using Stack:")
for element in D:
    print(element)
