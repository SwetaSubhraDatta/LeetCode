import math
def minimumCardPickup(cards: list) -> int:
    mp_freq={}
    l=0
    min_length=math.inf
    for r in range(0,len(cards)):
        mp_freq[cards[r]]=mp_freq.get(cards[r],0)+1
        while mp_freq[cards[r]]>1:# if consecutive cards are found
            min_length=min(r-l+1,min_length)
            mp_freq[cards[l]]-=1# delete the first card
            # if mp_freq[cards[l]]==0:
            #     mp_freq.pop(cards[l],None) #Not needed as we are looping until we have all ones
            l+=1#move the left pointer
    return min_length if min_length!=math.inf else -1

def main():
   d= minimumCardPickup(cards=[3,4,2,3,4,7])
   print(d)

main()