### Tanya Kadiyala
### CMSY-257-300
### Lab 3
### Problem 2

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.logicalSize = 0
        self.fill_value = fill_value
        for count in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        if new_item is not None and self.items[index] is None:
            self.logicalSize += 1
        elif new_item is None and self.items[index] is not None:
            self.logicalSize -= 1
        self.items[index] = new_item
    
    def size(self):
        return self.logicalSize
    
    def grow(self):
        current_capacity = len(self.items)
        new_capacity = current_capacity * 2
        for i in range(current_capacity, new_capacity):
            self.items.append(self.fill_value)
    
    def shrink(self):
        current_capacity = len(self.items)
        if current_capacity <= 2: 
            return
        
        if self.logicalSize < current_capacity // 4:
            new_capacity = max(2, current_capacity // 2)
            self.items = self.items[:new_capacity]

if __name__ == "__main__":
    arr = Array(2)
    arr[0] = "A"
    arr[1] = "B"

    print("Before grow:", arr, "Capacity:", len(arr))
    arr.grow()
    print("After grow:", arr, "Capacity:", len(arr))

    arr[1] = None
    arr[0] = None
    arr.logicalSize = 0
    arr.shrink()
    print("After shrink:", arr, "Capacity:", len(arr))