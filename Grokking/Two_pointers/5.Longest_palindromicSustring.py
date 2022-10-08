#find the longest palindromic substring in a string
def longest_palindromic_substring(s: str):
    p_sub=""
    if len(s)==0 and s==s[::-1]:
        return 0
    l=1
    for r in range(len(s)):
        #odd case, like "aba"
        if r-l >=1 and s[r-l-1:r+1]==s[r-l-1:r+1][::-1]:
            p_sub=s[r-l-1:r+1]
            l+=2
            continue
        #even case, like "abba"
        if r-l >=0 and s[r-l:r+1]==s[r-l:r+1][::-1]:
            p_sub=s[r-l:r+1]
            l+=1
    if l==1:
        return s[0]
    else: 
        return p_sub

        
    
    


        
        



  

        
        
         
def main():
    print(longest_palindromic_substring("bababaab"))
main()