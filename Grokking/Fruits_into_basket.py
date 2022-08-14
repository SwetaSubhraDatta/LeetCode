#Find maximum number of fruits in a basket

def totalFruit(fruits) -> int:
        fruits_count=0
        w_s=0
        mp_freq={}
        max_fruits=0

        for i  in range(0,len(fruits)):
          fruits_count+=1
          if fruits[i] not in mp_freq:
                mp_freq[fruits[i]]=0
          mp_freq[fruits[i]]+=1
          while len(mp_freq)>2:
                curr_char=fruits[w_s]
                mp_freq[curr_char]-=1
                if mp_freq[curr_char]==0:
                    mp_freq.pop(curr_char,None)
                w_s+=1
                fruits_count-=1
          max_fruits=max(max_fruits,fruits_count)
        return max_fruits
    
#Similar Problem

def longest_substring_with_2_distinct(s:str, k):
        length=0
        w_s=0
        mp_freq={}
        max_fruits=0

        for i  in range(0,len(s)):
          length+=1
          if s[i] not in mp_freq:
                mp_freq[s[i]]=0
          mp_freq[s[i]]+=1
          while len(mp_freq)>2:
                curr_char=s[w_s]
                mp_freq[curr_char]-=1
                if mp_freq[curr_char]==0:
                    mp_freq.pop(curr_char,None)
                w_s+=1
                length-=1
          max_fruits=max(max_fruits,length)
        return max_fruits

def main():
  print("Maximum number of fruits: " + str(totalFruit(fruits=['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(totalFruit(['A', 'B', 'C', 'B', 'B', 'C'])))

main()