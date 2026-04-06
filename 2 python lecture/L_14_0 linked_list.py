class node:
    def __init__(self, val):
        self.val = float(val)         # receiving float only
        self.next = None



head_1 = node(1)
head_2 = node(10)
head_3 = node(100)
head_4 = node(1000)


head_1.next = head_2
head_2.next = head_3
head_3.next = head_4

# inserting a new node in the middle
head_2_1 = node(10.10)          # creating a new node
head_2_1.next = head_2.next     # assigning all the elements after head_2 to after head_2_1
head_2.next = head_2_1          # now assigning head_2_1 to head_2


# adding some more new nodes
head_1_1 = node(1.10)
head_1_2 = node(1.20)
head_1_3 = node(1.30)

head_1_3.next = head_1.next
head_1.next = head_1_1
head_1_1.next = head_1_2
head_1_2.next = head_1_3



temp = head_1
while temp is not None:
    if temp.next is not None:
        print(temp.val, end=" -> ")
        temp = temp.next
    else:
        print(temp.val, end="")
        temp = temp.next




# Why Linked Lists can be better than Arrays / Python Lists

# 1. Efficient Insertion & Deletion
# - Linked Lists allow O(1) insertion and deletion (if you have the reference)
# - No shifting of elements required (unlike arrays/lists which are O(n))

# 2. Dynamic Size
# - Linked Lists grow/shrink dynamically
# - Arrays/lists may need resizing or reallocation (can be computationally heavy during very long array and list size)

# 3. Memory Utilization
# - No need for contiguous memory
# - Useful when memory is fragmented

# 4. No Wasted Capacity
# - Arrays often allocate extra space (over-allocation in Python lists)
# - Linked Lists allocate memory only when needed

# 5. Better for Frequent Modifications
# - If your use case involves frequent insert/delete operations,
#   linked lists are more efficient than arrays/lists

# ------------------------------------------------------------

# But keep in mind (limitations):

# - No random access (O(n) to access elements)
# - Extra memory for pointers (next references)
# - Slower traversal due to non-contiguous memory


