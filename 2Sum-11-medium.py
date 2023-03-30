from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int):
        numbers.sort()
        l, r = 0, len(numbers) - 1

        while r > l:
            curSum= numbers[l] + numbers[r]

            if curSum > target:
                r = r - 1
            elif curSum < target:
                l = l + 1
            else:
                return [l + 1, r + 1]
        return []
