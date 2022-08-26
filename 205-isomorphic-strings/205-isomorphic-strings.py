class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #if length of strings 's' and 't' are not the same return false
        if len(s) != len(t):
            return False
        
        
        #Use a dictionary(array) to store mapping from characters of string s to string t 
        d = {}
        
        #use a set to store a pool of already mapped characters
        p = set()
            
            
        for i in range(len(s)):
            S = s[i]
            T = t[i]
            
            #if 'S' is seen before
            if S in d: 
                #return false if the first occurance of 'S' is mapped to a different character
                if d[S] != T:
                    return False
                
            #if 'S' is seen for the first time (i.e. not mapped yet)
            else:
                #return false if 'T' is already mapped to some other char 'S'
                if T in p:
                    return False
                
                #map 'T' to 'S' and mark it as mapped
                d[S] = T
                p.add(T)
                
        return True
            