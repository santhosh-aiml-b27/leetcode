class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(len(s)):
            current=""
            for j in range(i,len(s)):
                if s[j] not in current:
                    current += s[j]
                else:
                    break
            if len(current)>l:
                l=len(current)
        return l