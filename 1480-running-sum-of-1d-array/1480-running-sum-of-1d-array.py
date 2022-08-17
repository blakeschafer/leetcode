class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #prefix ssum array running sums
        rs = [0] * len(nums)
        rs[0] = nums[0]
        #traverse through the array and add the previous index 
        #plus the current index to the new array
        for i in range(1, len(nums)):
            rs[i] = rs[i-1] + nums[i]
        return rs