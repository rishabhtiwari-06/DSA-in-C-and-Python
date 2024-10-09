#Remove Linked List Elements
#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
class ListNode:
    def __init__(self,val =0 ,next = None ) -> None:
        self.val = val
        self.next = next

class Solution:
    # def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    def removeElements(self, head: ListNode , val:int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
        current = head
        while current is not None and current.next is not None:
            if(current.next.val == val):
                current.next = current.next.next
            else:
                current = current.next
        return head

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

    head = create_linked_list([7,7,7,7])
    val = 7
    sol = Solution()
    middle_node = sol.removeElements(head , val)
    print_linked_list(middle_node)
    