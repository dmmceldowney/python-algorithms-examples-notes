# 1-3. All test stuff; not interested.

# 4. Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
import random


def kthSmallest(my_list, k=0):
    # sort the list
    my_list.sort()
    # get the kth entry
    return my_list[k]


l = []
for i in range(0, 10):
    l.append(random.randrange(0, 10))
print(kthSmallest(l, 5))

# 5. Can you implement this in a O(1) time? Explain.
"""
I don't think so. There aren't any list methods that allow for this in O(1) time due to the way lists work.
At least that's what my notes tell me.
"""