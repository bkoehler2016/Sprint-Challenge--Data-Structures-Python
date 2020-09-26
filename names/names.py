import time

class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
                
            else:
                self.left.insert(value)
                
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
                
            else:
                self.right.insert(value)
                
    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

bst = BSTNode("None")

for name in names_1:
    bst.insert(name)
    
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# first runtime: 5.158061742782593 seconds
# improvment runtime: 0.08058381080627441 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
