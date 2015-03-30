#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-26 17:54:40 Thursday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
# Given a string S, find the longest palindromic substring in S. You may
# assume that the maximum length of S is 1000, and there exists one unique
# longest palindromic substring.
################################################################################
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        s_len = len(s)
        if not s or s_len == 1:
            return ss
        max_pa_str = ""
        cursor = 0
        while cursor + (len(max_pa_str)/2)  < s_len:
            index = 0
            while cursor-index >= 0 and cursor+index+1 < s_len:
                if s[cursor-index] == s[cursor+index+1]:
                    index += 1
                else:
                    break
            if index*2 > len(max_pa_str):
                max_pa_str = s[cursor-index+1:cursor+index+1]
            index = 0
            while  cursor-index >= 0 and cursor+index < s_len:
                if s[cursor-index] == s[cursor+index]:
                    index += 1
                else:
                    break
            if (index*2-1) > len(max_pa_str):
                max_pa_str = s[cursor-index+1:cursor+index]
            cursor += 1
        return max_pa_str



if __name__ == "__main__":
    ss = "bbb"
    test_class = Solution()
    print test_class.longestPalindrome(ss)
