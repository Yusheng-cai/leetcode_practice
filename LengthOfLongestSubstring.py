# Author: Yusheng Cai
# Problem URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem Statement: Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        # stores the {index+1} of every one of the strings 
        mp = {}
        
        # The trailing index
        i = 0
        length = 0
        
        for j in range(len(s)):
            if s[j] in mp:
                # check which one is larger, the repeated index +1 or the current i
                i = max(mp[s[j]],i)
            
            length = max(length,j-i+1)
            mp[s[j]] = j +1
        
        return length
