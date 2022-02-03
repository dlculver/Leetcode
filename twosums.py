class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num+nums[j]==target:
                    return [i,j]
#### The above is a very brute force method. Here we go through all pairs and check which sum up to the target.
#### This code works, in part, because in the problem statement we are allowed to assume that there is a unique solution.
#### the computational complexity of this code is O(n^2), which is not very efficient. There is a more efficient code.
