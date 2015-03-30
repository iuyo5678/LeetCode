#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time-stamp: <2015-03-30 15:54:11 Monday by zhangguhua>

# @version 1.0
# @author zhangguhua

################################################################################
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#    P   A   H   N
#    A P L S I I G
#    Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#    string convert(string text, int nRows);
#    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
################################################################################

def map_func(a, b):
    if not a:
        a = ""
    if not b:
        b = ""
    return "".join([a, b])
        


class Solution:
    # @return a
    def convert(self, s, nRows):

        if len(s) <= 2 or nRows < 2:
            return s
        one_round = 2 * nRows - 2
        z_tag_result = []
        
        for i in range(0, one_round):
            temp_list = s[i::one_round]
            z_tag_result.append(temp_list)
            
        result_list = []
        result_list.append(z_tag_result[0])
        for i in range(1, nRows-1):
            temp_list = map(map_func, z_tag_result[i], z_tag_result[2*nRows-2-i])
            temp_list = "".join(temp_list)
            result_list.append(temp_list)
        result_list.append(z_tag_result[nRows-1])
        result = "".join(result_list)
        return result
    
        
if __name__ == "__main__":
    test_class = Solution()
    print test_class.convert("", 1)

