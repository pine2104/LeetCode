# https://leetcode.com/problems/reorder-list/
# https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained
# https://leetcode.com/problems/reorder-list/discuss/801971/Python-O(n)-by-two-pointers-w-Visualization
# https://leetcode.com/problems/reorder-list/discuss/567955/Python-2-solutions%3A-Stack-3-steps-Clean-and-Concise
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## first thought
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    temp = []
    root = head.next
    while root:
        temp.append(root)
        root = root.next

    for i in range(len(temp)):
        if i% 2 == 0:
            # from tail
            node = temp.pop()
        else:
            # from head
            node = temp.pop(0)
        # print(node.val)
        head.next = node
        head = head.next
    head.next = None

def reorderList2(head):

    """
    Do not return anything, modify head in-place instead.
    """
    # step 1: find middle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    prev = None
    while slow:
        temp = slow
        slow = slow.next
        temp.next = prev
        prev = temp

    # step 3: merge lists, prev and head
    # print(prev)
    temp_head = head
    temp_prev = prev
    # not append last one(double appending will cause cyclic linked list), because 1.append prev and 2.append head
    while temp_prev.next:
        # store head.next
        head_next = temp_head.next
        # assign next to prev
        temp_head.next = temp_prev
        # move temp_head to temp_head.next
        # temp_head = temp_prev # 1
        # or
        temp_head = temp_head.next # 2
        # assign head.next.next to previous head.next
        temp_prev = head_next