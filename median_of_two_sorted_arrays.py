#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-24 22:59:42 Tuesday by zhangguhua>

# @version 1.0
# @author zhangguhua
################################################################################
# There are two sorted arrays A and B of size m and n respectively. Find the
# median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
################################################################################


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        pass




# 偷懒的解法直接调用库函数
# class Solution:
#     # @return a float
#     def findMedianSortedArrays(self, A, B):
#         A.extend(B)
#         A.sort()
#         length = len(A)
#         if length%2 == 0:
#             return (A[length/2] + A[length/2 - 1])/2.0
#         else:
#             return A[int(length/2)]

if __name__ == "__main__":
    test_class = Solution()
    print test_class.pow(4.3, 10)
