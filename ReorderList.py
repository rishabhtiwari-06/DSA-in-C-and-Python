# class ListNode:
#     def __init__(self,val =0 ,next = None ) -> None:
#         self.val = val
#         self.next = next
# class Solution:
#     def reOrderList(self, head: ListNode ) -> ListNode:
#         slow,fast = head,head
#         while fast and fast.next:
#             slow= slow.next
#             fast = fast.next.next
#         prev = None
#         while slow:
#             next_node = slow.next
#             slow.next = prev
#             prev = slow
#             slow = next_node
#         left , right = head , prev
#         while right:
#             x = left.next
#             y = right.next
#             left.next = right
#             right = y
#             left =x
#         return head


# def create_linked_list(values):
#     if not values:
#         return None
#     head = ListNode(values[0])
#     current = head
#     for value in values[1:]:
#         current.next = ListNode(value)
#         current = current.next
#     return head

# def print_linked_list(head):
#     current = head
#     result = []
#     while current:
#         result.append(current.val)
#         current = current.next
#     print(result)

# if __name__ == "__main__":

#     head = create_linked_list([1,2,3,4])
#     sol = Solution()
#     reorder = sol.reOrderList(head)
#     print_linked_list(reorder)
    
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reOrderList(self, head: ListNode) -> None:
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reversing 2nd half 
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #Merging
        left, right = head, prev
        while right.next:
            x, y = left.next, right.next
            left.next = right
            right.next = x
            left = x
            right = y

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4])
    sol = Solution()
    sol.reOrderList(head)
    print_linked_list(head)

    head2 = create_linked_list([1, 2, 3, 4, 5])
    sol.reOrderList(head2)
    print_linked_list(head2)
