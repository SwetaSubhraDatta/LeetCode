def Dutch_National_flag(nums:list):
    lo,high=0,len(nums)-1
    i=0
    while(i<=high):
        if nums[i]==0:
            nums[i],nums[lo]=nums[lo],nums[i]
            lo+=1
            i+=1
        elif nums[i]==1:
            i+=1
        else:
            nums[i],nums[high]=nums[high],nums[i]
            high-=1
    return nums

def main():
    d=Dutch_National_flag(nums=[0,0,2,1,1,0,1,2,2,0])
    print(d)
main()
