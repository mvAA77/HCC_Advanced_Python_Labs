### Tanya Kadiyala
### CMSY-257-300
### Lab 3
### Problem 4

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
    
    def __eq__(self, other):
        if not isinstance(other, Array):
            return False
        
        if self.logicalSize != other.logicalSize:
            return False
        
        for i in range(self.logicalSize):
            if self.items[i] != other.items[i]:
                return False
        
        return True

# Test driver
if __name__ == "__main__":
    arr1 = Array(5)
    arr2 = Array(5)

    arr1[0], arr1[1], arr1[2] = 10, 20, 30
    arr2[0], arr2[1], arr2[2] = 10, 20, 30
    arr1.logicalSize = 3
    arr2.logicalSize = 3

    print("Are arrays equal?", arr1 == arr2)

    arr2[2] = 40
    print("Are arrays equal now?", arr1 == arr2)

    arr3 = Array(5)
    arr3[0], arr3[1] = 10, 20
    arr3.logicalSize = 2
    print("Different sizes equal?", arr1 == arr3)