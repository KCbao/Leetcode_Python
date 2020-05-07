# Leetcode_Python

- This is a repo for my personal training/practice on leetcode.

- Timeline: 
As up to April 11, 2020 - 57
As up to May 6, 2020 - 67

### List:
- `sorted(range(len(prices)), key=lambda k: prices[k])`

### Linked List:
- For array, memory has to be allocated in advance for a specific number of items in an array, when less items to fill all array index, memory space is wasted; when add or remove an item in array, memory locations has to be updated
- For linked list, whenever a new item is required to be added to the linked list, the memory for the new node is created at run time. for each item in memory location, linked list stores value of the item and the pointer to the next item. 
- 
```
tmp = ans
tmp = ListNode(1) # in memory, stores node1 = (val=1, pointer=None)
tmp.next = ListNode(2) # in memory, node1 = (val=1, pointer=Node 2), where node2=(val=2, pointer=None)
tmp = tmp.next # tmp moves from node1 to node2, but node 1 pointer remains unchanged, ans=node1->node2
```
