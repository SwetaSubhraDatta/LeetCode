# Find the longest distinct substring in a string


def longest_distinct_substring(s: str):
    mp_distinct=set()
    w_s=0
    max_length=0
    for i in range(0,len(s)):
        while s[i] in mp_distinct:
            mp_distinct.remove(s[w_s])
            w_s+=1
        mp_distinct.add(s[i])
        max_length=max(max_length,i-w_s+1)
    return max_length








if __name__ =="__main__":
    longest_distinct_substring("dvdf")

