class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
       #if not s return true
        if not s:
            return True
        
        i = 0
        
        #itrerating through every character in t
        #comparing it to each char in string s
        for c in t:
            if c == s[i]: #if c in t is found in string s go to next char
                i += 1
            if i >= len(s):#if we reached the end of string s end iteration
                break
                
        if i == len(s): #array i and string s should be identicial so return true
            return True
        
        return False
    
    #Time Complexity: O(N)
    #Space Complexity: O(1)
        