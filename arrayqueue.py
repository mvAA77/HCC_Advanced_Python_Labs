class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._rear = -1
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def clear(self):
        # remove all items using pop() to preserve any resizing logic
        while not self.is_empty():
            self.pop()
        # reset front and rear to initial positions
        self._front = 0
        self._rear = -1

    def add(self, item):
        if self._size == len(self._items):
            self._resize(2 * len(self._items))
        self._rear = (self._rear + 1) % len(self._items)
        self._items[self._rear] = item
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise KeyError("Queue is empty")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1
        if 0 < self._size < len(self._items) // 4:
            self._resize(len(self._items) // 2)
        return item

    def peek(self):
        if self.is_empty():
            raise KeyError("Queue is empty")
        return self._items[self._front]

    def _resize(self, capacity):
        old = self._items
        self._items = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._items[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        self._rear = self._size - 1

    def __str__(self):
        items = []
        walk = self._front
        for _ in range(self._size):
            items.append(self._items[walk])
            walk = (walk + 1) % len(self._items)
        return str(items)

    def clone(self):
        clone = ArrayQueue()
        walk = self._front
        for _ in range(self._size):
            clone.add(self._items[walk])
            walk = (walk + 1) % len(self._items)
        return clone