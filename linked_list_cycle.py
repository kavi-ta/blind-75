# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # assign the head to the current node
        current_node = head
        # METHOD: replace the value of current_node.val to True if visited
        while(current_node):
            # if the node is previsited, and the value is True=> there exists a loop
            if current_node.val is True:
                return True
            # since node visited for the first time, assign value to True
            current_node.val = True
            current_node = current_node.next
        return False