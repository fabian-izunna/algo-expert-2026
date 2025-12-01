class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_dict = {} #value : index

        for index, no in enumerate(nums):
            if no in no_dict:
                return True
            else:
                no_dict[no] = index

        return False
