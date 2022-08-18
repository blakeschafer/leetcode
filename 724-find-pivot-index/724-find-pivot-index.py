class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #the total of nums
        totalSum = sum(nums) #O(n)
        #create variable for left sum
        leftSum = 0
        #iterate through the length of the array
        for i in range(len(nums)):
            #compute the right sum, total - current index - left sum = right sum, 28-6-11=11
            # if left sum equals right sum, we found our pivot index so return it
            rightSum = totalSum - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            #move to the next index
            leftSum += nums[i]
        #else return -1
        return -1
        