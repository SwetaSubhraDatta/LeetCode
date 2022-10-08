        
def containsDuplicate(nums):
        mp={}
        for i in range(len(nums)):
            mp[nums[i]]=mp.get(nums[i],0)+1 
            if mp[nums[i]]>1:
                return True
        return False
#Using set
def containsDuplicate(nums):
    return len(set(nums))!=len(nums)


def main():
    print(containsDuplicate([1,2,3,1]))

main()