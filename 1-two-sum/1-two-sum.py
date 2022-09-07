class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #list to store results
        result = []
        
        #dictionary to store the difference and its index
        index_map = {}
        
        #itertate through nums array(list)
        for i, n in enumerate(nums):
            #difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
            
        #return the results array with the answer in it ]
        return result
            