class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # index (i) : val (n)

        for i, n in enumerate(nums): # got through the index and vals for nums
            diff = target - n  # first find the num needed in hasMap from diff using target changes w each new n
            if diff in hashMap:  # num is found in hashMap ~
                return [hashMap[diff], i] # this gives the indices: [hashMap[diff], current i] 
            hashMap[n] = i # add the val and index to hashMap
        return


        