class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing = {} # value:index
        
        for index, no in enumerate(nums):
            diff = target - no
            if diff in hashing:
                return hashing[diff], index
            else:
                hashing[no] = index
