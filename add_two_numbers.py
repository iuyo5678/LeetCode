#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-27 19:16:23 Friday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
#   You are given two linked lists representing two non-negative numbers. The
# digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
################################################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        carry_tag = 0
        point_l1 = l1
        point_l2 = l2
        while True:
            sum = point_l1.val + point_l2.val + carry_tag
            if sum >= 10:
                carry_tag = 1
            else:
                carry_tag = 0

            point_l1.val = sum % 10

            if not point_l1.next:
                if not point_l2.next:
                    if carry_tag != 0:
                        point_l1.next = ListNode(carry_tag)
                        carry_tag = 0
                    return l1
                else:
                    if carry_tag != 0:
                        point_l1.next = ListNode(carry_tag)
                        carry_tag = 0
                    else:
                        point_l1.next = point_l2.next
                        return l1
            if not point_l2.next:
                if carry_tag != 0:
                    point_l2.next = ListNode(carry_tag)
                    carry_tag =0
                else:
                    return l1
                    
            point_l1 = point_l1.next
            point_l2 = point_l2.next

if __name__ == "__main__":
    test_class = Solution()
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l2 = ListNode(1)
    result = test_class.addTwoNumbers(l2, l1)
    print result.val
    while result.next:
        result = result.next
        print result.val
