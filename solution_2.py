'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:



    def addTwoNumbers(self, l1, l2):
        list_1 = []
        list_2 = []
        list_1.append(l1.val)
        list_2.append(l2.val)
        while l1.next != None:
            list_1.append(l1.next.val)
            l1 = l1.next
        while l2.next != None:
            list_2.append(l2.next.val)
            l2 = l2.next
        list_1.reverse()
        list_2.reverse()
        list_3 = int(''.join(str(x) for x in list_1))+int(''.join(str(x) for x in list_2))

        value =[x for x in str(list_3)]
        result = [None]*len(value)
        for i in range(0,len(value)):
            result[i] = ListNode()
            result[i].val = value[i]
        result.reverse()
        for i in range(0,len(value)-1):
            result[i].next=result[i+1]


        return result[0]
