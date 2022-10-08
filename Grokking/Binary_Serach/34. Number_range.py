
#find the first and last position of an element in a sorted array

def find_range(nums,target):
    first_occurence=binary_search(nums,target,need_to_find_start=True)
    last_occurence=binary_search(nums,target,need_to_find_start=False)
    ans=[first_occurence,last_occurence]
    return ans



def binary_search(nums,target,need_to_find_start:bool):
    ans=-1
    start,end=0,len(nums)-1
    while(start<=end):
        mid=(start+end)//2
        if nums[mid]<target:
            start=mid+1
        elif nums[mid]>target:
            end=mid-1 # Remember you are moving the mid pointer
        else:
            ans=mid
            #Got the value which is equal to mid but this is a potential answer
            if (need_to_find_start):
                end=mid-1 
            else:
                start=mid+1
    return ans        

def main():
    arr,target=[1,3,3,3,3,3,7,6],3
    print(find_range(nums=arr,target=target))

main()