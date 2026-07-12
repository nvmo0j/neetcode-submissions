class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 # start of str
        r = len(s) - 1 # end of str

        l = 0 # start of str ~
        r = len(s) - 1 # end of str ~
        
        while l < r:    # iterate over the str until it meets
            while l < r and not s[l].isalnum(): # skip non-alphanum and increment to the next iteration (left)
               l += 1
            while l < r and not s[r].isalnum():  # skip non-alphanum and decrement to prev iteration (right)
                r -= 1
            if s[l].lower() != s[r].lower():   # if the left lowercase and right lowercase diff ~ False 
                return False
            l +=1; r -= 1 # match is found ~ pointers comer inward and meet
        return True # valid Palindrome when no mismatches are found


       
        