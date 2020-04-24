import time
from lru_cache import LRUCache
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

## Iterative / nested loops:
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Run time: O(n^2) - 5.5 seconds


lru_Cache = LRUCache(10000)
## using LRU Cache:
# for name1 in names_1:
#     lru_Cache.set(name1, name1)
# for name2 in names_2:
#     if lru_Cache.get(name2):
#         duplicates.append(name2)

# Run time: O(n) - 0.028 seconds


bst = BinarySearchTree(names_1[0])
## using Binary Search Tree:
for name1 in names_1:
    bst.insert(name1)
for name2 in names_2:
    if bst.contains(name2):
        duplicates.append(name2)

# Run time: O(n) - 0.103 seconds


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")






# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
