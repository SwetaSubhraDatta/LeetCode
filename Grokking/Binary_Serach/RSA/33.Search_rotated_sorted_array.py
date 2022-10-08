
# Search in rotated sorted array that contains duplicates as well as distinct elements


from typing import List
class RSA:
    #Use this if the nature of the array is already known
    def __init__(self,is_duplicate:bool,is_rotated:bool) -> None:
        self.is_duplicate=is_duplicate
        self.is_rotated=is_rotated
        
    def search_in_rsa(self,nums,target,start,end):
        start,end=0,len(nums)-1
        start_element,end_element=nums[0],nums[len(nums)-1]
        if not self.is_duplicate:
            pivot=self.find_pivot_in_distinct_rsa(nums,start,end)
        else:
            pivot=self.find_pivot_in_duplicate_rsa(nums,start,end)
        ##3 cases
        #1. target is pivot

        if pivot==-1:
            return self.simple_binary_search(nums,target,0,len(nums)-1)
        elif nums[pivot]==target:
            return pivot
        #2. target is more than start but pivot is not null
        elif target>=start_element and pivot!=-1:
            return self.simple_binary_search(nums,target,0,pivot+1)
        elif target<start_element and pivot!=-1: #3. target is less than pivot and pivot is not null
            return self.simple_binary_search(nums,target,pivot+1,len(nums)-1)
        else:
            return -1   
        
    def find_pivot_in_distinct_rsa(self,nums,start,end):
        while(start<end):
            mid=(start+end)//2
            if mid<end and nums[mid]>nums[mid+1] :
                return mid
            elif nums[mid]<nums[mid-1] and mid>start:
                return mid-1 #return the previous element
            elif nums[start]>=nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return -1

    def find_pivot_in_duplicate_rsa(self,nums,start,end):
        while(start<=end):
            mid=(start+end)//2
            if mid<end and nums[mid]>nums[mid+1] :
                return mid
            elif mid>start and nums[mid]<nums[mid-1]:
                return mid-1
            elif nums[start]==nums[mid] and  nums[mid]==nums[end]:

                #Check iff the start and end are the pivot
                if start<end and nums[start]>nums[start+1]:
                    return start
                elif end > start and nums[end]<nums[end-1]:
                    return end-1
                else:
                    start+=1
                    end-=1
            elif nums[start]<nums[mid] or nums[start]==nums[mid] and nums[mid]>nums[end]:
                    start=mid+1
            else:
                    end=mid-1
        return -1

    
    def check_duplicate(self,nums):
        return False
    
    def check_rotated(self,nums):
        return False
    
    def check_sorted(self,nums):
        return False
    
    def count_rotations(self,nums):
        return 0

    def simple_binary_search(self,nums,target,start,end):
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1
    
    
def main():
    arr,target=[2,2,2,3,1],1
    rsa=RSA(is_duplicate=True,is_rotated=True)
    print(rsa.search_in_rsa(arr,target,0,len(arr)-1))
main()