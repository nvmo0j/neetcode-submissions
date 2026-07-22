class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
        