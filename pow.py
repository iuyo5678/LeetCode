#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-21 22:19:12 Saturday by zhangguhua>

# @version 1.0
# @author zhangguhua

#Implement pow(x, n)

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return pow(1/x , 0-n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return pow(x*x, n/2)
        else:
            return x * pow(x*x, (n-1)/2)

if __name__ == "__main__":
    test_class = Solution()
    print test_class.pow(4.3, 10)
