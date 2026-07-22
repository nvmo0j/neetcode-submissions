class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time & space: O(n)
        charS = set()   # checks for dupes in substrs
        l = 0   # left pointer
        longest = 0  # holds longest substring length

        for r in range(len(s)):    # right pointer checks runs until OOB
            while s[r] in charS:  # check if a dupe is found ~
                charS.remove(s[l])    # found: remove the left char
                l += 1   # slide the left pointer over to next char
            charS.add(s[r])     # right char is added to the set for checking
            longest = max(longest, r - l + 1)    # find the longest length ~
        return longest   # return len of the longest substring w/o dupes
        