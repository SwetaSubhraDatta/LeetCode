def isSubsequence(s:str,t:str):
        s_pointer=0
        if len(s)>len(t): #Not a subsequence see Wikipedia Page on Subsequence defination
            return False

        for t_pointer in range(len(t)): #first go through the main string string
            if s_pointer==len(s): # Early Stop injection
                return True
            if t[t_pointer]==s[s_pointer]: #go through the second string
                    s_pointer+=1 #If the element is found in the second string, increase the pointer
        return s_pointer==len(s) #If the pointer is equal to the length of the second string, a valid subsequence is Found return true
        
    


def main():
    print(isSubsequence("abc","ahbgdc"))

main()