class ArrayQueue:
    """Array-based implementation of a queue."""
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        """Initialize an empty queue."""
        self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        class ArrayQueue:
            """Array-based implementation of a queue collection."""

            DEFAULT_CAPACITY = 10

            def __init__(self):
                """Initialize an empty queue."""
                self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
                self._size = 0
                self._front = 0
                self._rear = -1

            def add(self, item):
                """Adds item to the rear of the queue."""
                if self._size == len(self._items):
                    self._resize(2 * len(self._items))

                self._rear = (self._rear + 1) % len(self._items)
                self._items[self._rear] = item
                self._size += 1

            def pop(self):
                """
                Removes and returns the front item from the queue.
                Raises KeyError if the queue is empty.
                """
                if self.is_empty():
                    raise KeyError("Queue is empty")

                item = self._items[self._front]
                self._items[self._front] = None  # Help garbage collection
                self._front = (self._front + 1) % len(self._items)
                self._size -= 1

                # Shrink the array if it's too empty
                if 0 < self._size < len(self._items) // 4:
                    self._resize(len(self._items) // 2)

                return item

            def peek(self):
                """
                Returns the front item from the queue without removing it.
                Raises KeyError if the queue is empty.
                """
                if self.is_empty():
                    raise KeyError("Queue is empty")
                return self._items[self._front]

            def clear(self):
                """Makes the queue become empty."""
                self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
                self._size = 0
                self._front = 0
                self._rear = -1

            def is_empty(self):
                """Returns True if the queue is empty."""
                return self._size == 0

            def __len__(self):
                """Returns the number of items in the queue."""
                return self._size

            def _resize(self, capacity):
                """Resize the internal array to the specified capacity."""
                old_items = self._items
                self._items = [None] * capacity
                walk = self._front

                for i in range(self._size):
                    self._items[i] = old_items[walk]
                    walk = (walk + 1) % len(old_items)

                """
                Array Queue Implementation
                CMSY 257 - Lab 6 - Problem 2
                """

                class ArrayQueue:
                    """Array-based implementation of a queue collection."""
    
                    DEFAULT_CAPACITY = 10
    
                    def __init__(self):
                        """Initialize an empty queue."""
                        self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
                        self._size = 0
                        self._front = 0
                        self._rear = -1
    
                    def add(self, item):
                        """Adds item to the rear of the queue."""
                        if self._size == len(self._items):
                            self._resize(2 * len(self._items))
        
                        self._rear = (self._rear + 1) % len(self._items)
                        self._items[self._rear] = item
                        self._size += 1
    
                    def pop(self):
                        """
                        Removes and returns the front item from the queue.
                        Raises KeyError if the queue is empty.
                        """
                        if self.is_empty():
                            raise KeyError("Queue is empty")
        
                        item = self._items[self._front]
                        self._items[self._front] = None  # Help garbage collection
                        self._front = (self._front + 1) % len(self._items)
                        self._size -= 1
        
                        # Shrink the array if it's too empty
                        if 0 < self._size < len(self._items) // 4:
                            self._resize(len(self._items) // 2)
        
                        return item
    
                    def peek(self):
                        """
                        Returns the front item from the queue without removing it.
                        Raises KeyError if the queue is empty.
                        """
                        if self.is_empty():
                            raise KeyError("Queue is empty")
                        return self._items[self._front]
    
                    def clear(self):
                        """Makes the queue become empty."""
                        self._items = [None] * ArrayQueue.DEFAULT_CAPACITY
                        self._size = 0
                        self._front = 0
                        self._rear = -1
    
                    def is_empty(self):
                        """Returns True if the queue is empty."""
                        return self._size == 0
    
                    def __len__(self):
                        """Returns the number of items in the queue."""
                        return self._size
    
                    def _resize(self, capacity):
                        """Resize the internal array to the specified capacity."""
                        old_items = self._items
                        self._items = [None] * capacity
                        walk = self._front
        
                        for i in range(self._size):
                            self._items[i] = old_items[walk]
                            walk = (walk + 1) % len(old_items)
        
                        self._front = 0
                        self._rear = self._size - 1
    
                    def __str__(self):
                        """Returns string representation of the queue from front to rear."""
                        items = []
                        walk = self._front
                        for _ in range(self._size):
                            items.append(str(self._items[walk]))
                            walk = (walk + 1) % len(self._items)
                        return "[" + ", ".join(items) + "]"
    
                    def clone(self):
                        """Returns a copy of the current queue."""
                        new_queue = ArrayQueue()
                        walk = self._front
                        for _ in range(self._size):
                            new_queue.add(self._items[walk])
                            walk = (walk + 1) % len(self._items)
                        return new_queue
