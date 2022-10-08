#4sum

def foursum(nums:list,target:int):
    nums.sort() #sort the array
    res=[] #empty list to store the result
    for x in range(len(nums)):
        if x>0 and nums[x]==nums[x-1]:
            continue
        for y in range(x+1,len(nums)):
            if y>x+1 and nums[y]==nums[y-1]:
                continue
            l,r=y+1,len(nums)-1
            while l<r:
                current_sum=nums[x]+nums[y]+nums[l]+nums[r]
                if current_sum==target:
                    res.append([nums[x],nums[y],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif current_sum<target:
                    l+=1
                else:
                    r-=1
    return res
def main():
    print(foursum([-5, 0, 2, 3,3,2,2]))
main()


