#Remove duplicates from a sorted array
def remove_duplicates(nums):
        k=1
        l=k
        if len(nums)<k:
            return len(nums)
        for r in range(l,len(nums)): #Given array is sorted
            if nums[r]!=nums[l-k]: #if current element is not equal to the previous K elements
                nums[l]=nums[r] #Than swap or delete the element
                l=l+1 #Increase K
        return l