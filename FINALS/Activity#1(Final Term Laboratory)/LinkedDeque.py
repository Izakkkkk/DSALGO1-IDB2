# LinkedDeque.py

from DoublyLinkedBase import _DoublyLinkedBase

class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue (Deque) implementation using a doubly linked list.'''

    def first(self):
        '''Return but do not remove the element at the front of the deque.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._header._next._element  # real item just after header

    def last(self):
        '''Return but do not remove the element at the back of the deque.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        '''Add an element to the front of the deque.'''
        self._insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        '''Add an element to the back of the deque.'''
        self._insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        '''Remove and return the element from the front of the deque.'''
        '''Raise Exception if the deque is empty.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        '''Remove and return the element from the back of the deque.'''
        '''Raise Exception if the deque is empty.'''
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._delete_node(self._trailer._prev)  # use inherited method

    #-------------------- Make the Deque Iterable --------------------
    def __iter__(self):
        '''Return an iterator for the deque.'''
        current = self._header._next  # Start with the first real element
        while current is not self._trailer:  # Iterate until the trailer
            yield current._element  # Yield each element one by one
            current = current._next  # Move to the next node
