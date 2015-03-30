#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-30 17:57:15 Monday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
# Given a list of non negative integers, arrange them such that they form the
# largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of
# an integer.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
################################################################################

def custom_cmp(a, b):
    str_a = "".join([a, b])
    str_b = "".join([b, a])
    return cmp(str_a, str_b)
    
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        result = []
        zero_tag = False
        for item in num:
            result.append(str(item))
            
        result = sorted(result, cmp=custom_cmp, reverse=True)
        result = "".join(result)
        return str(int(result))


if __name__ == "__main__":
    test_class = Solution()
    result = test_class.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])
    print result
