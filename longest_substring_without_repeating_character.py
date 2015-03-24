#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-24 22:16:02 Tuesday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
# Given a string, find the length of the longest substring without repeating
# characters. For example, the longest substring without repeating letters for
# "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
# is "b", with the length of 1.
################################################################################

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        gaurd_set = set()
        str_length = len(s)
        start = 0
        end = 0
        max_length = 1
        temp_length = 0

        if str_length == 0:
            return 0
        while end < str_length:
            alphabet = s[end]
            if alphabet not in gaurd_set:
                end += 1
                temp_length += 1
                if max_length <= temp_length:
                    max_length = temp_length
                gaurd_set.add(alphabet)
            else:
                while alphabet in gaurd_set and start < end:
                    gaurd_set.remove(s[start])
                    start +=1
                    temp_length -= 1

        return max_length

if __name__ == "__main__":
    test_class = Solution()
    ss = "bbbbbdaouoaiuodksfkajlfjfljlsdjflajlfjlajfldjl"
    #ss = "abcabcbbadkja;jkfdjldjasldflsjfkajslfja;uroqlkaf;nvaan,fnaoreuqowruoqn,n,snsv,mnv,zcn,nz,nv,n,"
    result = test_class.lengthOfLongestSubstring(ss)
    print result
