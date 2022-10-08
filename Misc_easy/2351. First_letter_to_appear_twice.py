 #first letter to appear twice

def repeated_Chars(s):
    mp={}
    for i in range(len(s)):
        if s[i] in mp:
            return s[i]
        mp[s[i]]=mp.get(s[i],0)+1
    return None

def main():
    print(repeated_Chars("abccbaacz"))

main()