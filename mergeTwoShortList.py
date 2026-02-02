
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def mergeTwoLists(self,list1,list2):
        dummy=ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
                
            current = current.next

        if list1:
            current.next=list1
        else:
            current.next=list2
        return dummy.next

# list1 = 1 -> 3 -> 5
list1 = ListNode(1, ListNode(3, ListNode(5)))

# list2 = 2 -> 4 -> 6
list2 = ListNode(2, ListNode(4, ListNode(6)))

sol = Solution()
result = sol.mergeTwoLists(list1, list2)
while result:
    print(result.val, end=" -> ")
    result = result.next


