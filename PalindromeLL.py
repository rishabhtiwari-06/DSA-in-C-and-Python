
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next 
        #Reversing the second half 
        prev = None
        while slow:
            next_node = slow.next 
            slow.next = prev
            prev = slow
            slow = next_node   
        #Comparing
        left , right = head , prev  
        while right:
            if left.val != right.val:
                return False
            left = left.next 
            right = right.next
        return True

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# def print_linked_list(head):
#     current = head
#     result = []
#     while current:
#         result.append(current.val)
#         current = current.next
#     print(result)

if __name__ == "__main__":

    head = create_linked_list([1, 2])
    sol = Solution()
    isPalindrome = sol.isPalindrome(head)
    print(isPalindrome)
    
  
