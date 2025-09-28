### Tanya Kadiyala
### CMSY-257-300
### Lab 3
### Problem 3


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
        return str([item for item in self.items if item is not None])
    
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
    
    def insert(self, position, item):
        if position >= self.logicalSize:
            if self.logicalSize < len(self.items):
                self.items[self.logicalSize] = item
                self.logicalSize += 1
            else:
                self.grow()
                self.items[self.logicalSize] = item
                self.logicalSize += 1
        else:
            if self.logicalSize == len(self.items):
                self.grow()
            
            for i in range(self.logicalSize, position, -1):
                self.items[i] = self.items[i-1]
            
            self.items[position] = item
            self.logicalSize += 1
    
    def pop(self, position):
        if position < 0 or position >= self.logicalSize:
            raise IndexError("Index out of bounds")
        
        popped_item = self.items[position]
        
        for i in range(position, self.logicalSize - 1):
            self.items[i] = self.items[i+1]
        
        self.items[self.logicalSize - 1] = self.fill_value
        self.logicalSize -= 1
        
        self.shrink()
        
        return popped_item
    
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

# Test driver
if __name__ == "__main__":
    arr = Array(5)
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    arr.logicalSize = 3

    print("Before insert:", arr)
    arr.insert(1, 99)
    print("After insert at index 1:", arr)

    popped = arr.pop(2)
    print("Popped value:", popped)
    print("After pop:", arr)