#Longest ones after replacing k0s

def longestOnes(self, nums: List[int], k: int) -> int:
    l,max_one_count=0,0
    max_length=0
    for r in range(0,len(nums)):
        if nums[r]==1:
            max_one_count+=1
        while(r-l+1)-max_one_count>k:
            if nums[l]==1:
                max_one_count-=1
            l+=1
        max_length=max(max_length,r-l+1)
    return max_length
            

