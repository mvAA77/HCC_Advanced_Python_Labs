class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def clear(self):
        # remove all nodes one by one so any cleanup in pop() runs
        while not self.is_empty():
            self.pop()

    def add(self, item):
        node = _QueueNode(item)
        if self._rear is None:
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise KeyError("Queue is empty")
        class _QueueNode:
            """Internal node for LinkedQueue."""

            def __init__(self, item):
                self.item = item
                self.next = None


        class LinkedQueue:
            """Linked implementation of a queue collection."""

            def __init__(self):
                self._front = None
                self._rear = None
                self._size = 0

            def is_empty(self):
                return self._size == 0

            def __len__(self):
                return self._size

            def clear(self):
                # remove all nodes one by one so any cleanup in pop() runs
                while not self.is_empty():
                    self.pop()

            def add(self, item):
                node = _QueueNode(item)
                if self.is_empty():
                    self._front = node
                else:
                    self._rear.next = node
                self._rear = node
                self._size += 1

            def pop(self):
                if self.is_empty():
                    raise KeyError("Queue is empty")
                item = self._front.item
                self._front = self._front.next
                if self._front is None:
                    self._rear = None
                self._size -= 1
                return item

            def peek(self):
                if self.is_empty():
                    raise KeyError("Queue is empty")
                return self._front.item

            def __str__(self):
                items = []
                current = self._front
                while current is not None:
                    items.append(str(current.item))
                    current = current.next
                return "[" + ", ".join(items) + "]"

            def clone(self):
                clone = LinkedQueue()
                current = self._front
                while current is not None:
                    clone.add(current.item)
                    current = current.next
                return clone