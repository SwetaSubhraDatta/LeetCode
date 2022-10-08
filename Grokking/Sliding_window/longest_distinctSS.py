# Find the longest distinct substring in a string


def longest_distinct_substring(s: str):
    mp_distinct=set()
    l=0
    max_length=0
    for r in range(0,len(s)):
        while s[r] in mp_distinct:
            mp_distinct.remove(s[l])
            l+=1
        mp_distinct.add(s[r])
        max_length=max(max_length,r-l+1)
    return max_length








if __name__ =="__main__":
    longest_distinct_substring("dvdf")

