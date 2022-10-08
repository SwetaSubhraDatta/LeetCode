#  triplet in the array whose sum is as close to the target number as possibl
import math
def threesum_closest(nums,target):
    nums=sorted(nums)
    max_diff=math.inf
    sum_min=0
    for x in range (len(nums)):
        if x>0 and nums[x]==nums[x-1]:
            continue
        l,r=x+1,len(nums)-1
        while(l<r):
            sum_current=nums[x]+nums[l]+nums[r]
            diff=abs(target - sum_current)
            if max_diff>diff:
                max_diff=diff
                sum_min=sum_current
            if sum_current<target:
                l+=1
                while(l<r and nums[l]==nums[l-1]):
                    l+=1
            else:
                r-=1
    return sum_min

def main():
    d=threesum_closest([0,0,0],1)
    print(d)
                
main()