from linkedqueue import LinkedQueue
from arrayqueue import ArrayQueue

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