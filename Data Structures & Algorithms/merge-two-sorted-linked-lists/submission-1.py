# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        starting_list = list2 if list1.val >= list2.val else list1
        other_list = list1 if list1.val >= list2.val else list2

        ret_value = starting_list

        while other_list and starting_list:
            if not starting_list.next or starting_list.next.val > other_list.val:
                tmp_other = other_list.next
                other_list.next = starting_list.next
                starting_list.next = other_list
                other_list = tmp_other
                starting_list = starting_list.next
            else:
                starting_list = starting_list.next
        
        return ret_value


