class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #### to get O(n) time we will create a dictionary which records the integers appearing in nums and where they appear. We then check whether the number target-nums[index] appears in the dictionary. The point is that scanning a list is O(n).
        numbersappearing = {}
        for index, number in enumerate(nums):
            if target-number in numbersappearing:
                return [numbersappearing[target-number], index]
            else:
                numbersappearing[number] = index
