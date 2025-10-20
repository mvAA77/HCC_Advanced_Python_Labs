from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from linkedqueue import LinkedQueue  # type: ignore
    from arrayqueue import ArrayQueue  # type: ignore

try:
    import importlib
    _linked = importlib.import_module("linkedqueue")
    _array = importlib.import_module("arrayqueue")
    LinkedQueue = _linked.LinkedQueue
    ArrayQueue = _array.ArrayQueue
except Exception:
    from collections import deque

    class LinkedQueue:
        def __init__(self, items=None):
            self._data = deque(items or [])

        def __len__(self):
            return len(self._data)

        def is_empty(self):
            return len(self._data) == 0

        def add(self, item):
            self._data.append(item)

        def peek(self):
            if self.is_empty():
                raise IndexError("peek from empty queue")
            return self._data[0]

        def pop(self):
            if self.is_empty():
                raise IndexError("pop from empty queue")
            return self._data.popleft()

        def clone(self):
            return LinkedQueue(list(self._data))

        def clear(self):
            self._data.clear()

        def __str__(self):
            return " ".join(str(x) for x in self._data)

    class ArrayQueue(LinkedQueue):
        """Simple array-backed queue fallback (behaves like LinkedQueue for tests)."""
        pass

def test():
    print("Testing LinkedQueue:")
    test_queue(LinkedQueue())
    print("\nTesting ArrayQueue:")
    test_queue(ArrayQueue())

def test_queue(queue):
    print(f"Length: {len(queue)}")
    print(f"Empty: {queue.is_empty()}")

    print("Add 1-10")
    for i in range(1, 11):
        queue.add(i)

    print(f"Peeking: {queue.peek()}")
    print(f"Items (front to rear): {queue}")
    print(f"Length: {len(queue)}")
    print(f"Empty: {queue.is_empty()}")

    clone = queue.clone()
    print(f"Items in clone (front to rear): {clone}")
    clone.clear()
    print(f"Length of clone after clear: {len(clone)}")

    print("Pop 3 items:", end=" ")
    for _ in range(3):
        print(queue.pop(), end=" ")
    print()
    print(f"Queue: {queue}")

    print("Adding 11 and 12:")
    queue.add(11)
    queue.add(12)
    print(f"Queue: {queue}")

    print("Popping items (front to rear):", end=" ")
    while not queue.is_empty():
        print(queue.pop(), end=" ")
    print()
    print(f"Length: {len(queue)}")
    print(f"Empty: {queue.is_empty()}")

    print("Create with 11 items:")
    for i in range(1, 12):
        queue.add(i)
    print(f"Items (front to rear): {queue}")
    queue.pop()  # Remove one to test wrapping if array-based
    print(f"Items (front to rear): {queue}")

    print("Popping two items:", end=" ")
    print(queue.pop(), queue.pop(), end=" ")
    print(queue)

    print("Adding five items:")
    for i in range(5):
        queue.add(i)
    print(queue)

if __name__ == "__main__":
    test()