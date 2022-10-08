#find uinque 3 elements in an array that sums to 0




def threesum_hashmap(nums): #accepted with 6s runtime for 450 testcase
    seen=set()
    mp={}
    nums=sorted(nums) #Step 1: Sort
    for i in range(len(nums)):
        mp[nums[i]]=i #Step 2: add to map
    for j in range(len(nums)):
        x=nums[j] #X=nums[0]--> nums[n-1]
        for k in range(j+1,len(nums)): #Y nums[n+1]-->nums[n] #Step 3: find the complement
            y=nums[k]
            z=0-x-y #find Z
            if z in mp and mp[z]>k: #if Z is in the map and the index of Z is greater than k
                  seen.add((x,y,z))
    return list(map(list,seen))   

def threesum_two_pointers(nums):
    triplets=[]
    nums=sorted(nums)
    #Step1 : Sort the array
    for x in range(len(nums)):
        if x>0 and nums[x]==nums[x-1]:# if it is not the first element and the previous element is the same as the current element
            continue #skip the current element
        l,r=x+1,len(nums)-1 #l=x+1,r=n-1
        while(l<r):
            target=nums[x]+nums[l]+nums[r]
            if target>0: #if the sum is greater than 0
                r-=1 #move the right pointer to the left to reduce the sum
            elif target<0: #if the sum is less than 0
                l+=1
            elif target==0:
                triplets.append([nums[x],nums[l],nums[r]])
                l+=1
                while(l<r and nums[l]==nums[l-1]): #Keep l<r first preventing overflow/out of index error and then check if the next element is the same as the current element
                    l+=1 #skip the duplicate elements right will shift automaticall
    return triplets


            


def main():
    res=threesum_two_pointers([-5,-4,5,0])
    print(res)

main()
        

