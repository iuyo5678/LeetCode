#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-27 17:31:16 Friday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
#Given  an array of integers, find two numbers such that they add up to a
#specific target number.

# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2. Please
# note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
################################################################################

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        """
        先将list转化为set
        将时间复杂度从O(n^2)变为O(n),
        空间换时间
        """
        find_tag = False
        tem_num_set = set(num)
        num_length = len(num)
        
        for i in range(0, num_length):
            difference = target - num[i]
            if difference in tem_num_set:
                for j in range(i+1, num_length):
                    if num[j] == difference:
                        find_tag = True
                        break

                if find_tag:
                    return (i+1, j+1)

if __name__ == "__main__":
    test_class = Solution()
    print test_class.twoSum([3, 2, 4, 5, 6, 4, 7], 11)

