class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case 1
        if s==t:
            return True
        map_strings={}
        map_strings_t={}
        count=0
        for each_string in s:
            if each_string in map_strings:
                map_strings[each_string]+=1
                continue
            map_strings[each_string]=count+1
        
        for each_string in t:
            if each_string in map_strings_t:
                map_strings_t[each_string]+=1
                continue
            map_strings_t[each_string]=count+1
        
        if map_strings_t==map_strings:  
            return True
        return False
            
if __name__=="__main__":
    soln=Solution()
    print(soln.isAnagram("ab","a"))