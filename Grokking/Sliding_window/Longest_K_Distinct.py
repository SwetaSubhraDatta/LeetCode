
def longest_substring_with_k_distinct(str1, k):
    length=0
    max_length=0
    w_s=0
    mp_freq={}
    for i in range(0,len(str1)):
        length=length+1
        if str1[i] not in mp_freq:
            mp_freq[str1[i]]=0
        mp_freq[str1[i]]+=1

        while len(mp_freq)>k:
            curr_char=str1[w_s]
            mp_freq[curr_char]-=1
            if mp_freq[curr_char]==0:
                mp_freq.pop(curr_char,None)
            w_s+=1
            length=length-1
        max_length=max(max_length,length)
    return max_length



def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()