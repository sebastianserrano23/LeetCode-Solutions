from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # intialize left pointer at 1
        l = 1

        # intialize right pointer at 1, we will be traversing through the list with this pointer
        for r in range(1, len(nums)):
            # comparing the index at r with the index at r - 1 (the previous index)
            if nums[r] != nums[r - 1]:
                #set the new value r at the position where l is pointing to
                nums[l] = nums[r]
                # incremenet left pointer
                l += 1
        return l
