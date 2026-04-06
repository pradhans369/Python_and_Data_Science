class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Setup the Anchor
        dummy = ListNode()
        tail = dummy
        
        # 2. The Zipper Loop
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            # Move our back-pointer forward
            tail = tail.next
            
        # 3. Attach the Leftovers
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # 4. Return the new Train
        return dummy.next
