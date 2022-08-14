# Removing duplicates from a sorted array
def remove_duplicates_method_1(arr):
    l=0
    for r in range(1,len(nums)):
        if nums[r]!=nums[l]:
            l+=1
            nums[l]=nums[r]
    return l+1



def remove_duplicates_generic(nums):
        k=1
        l=k
        if len(nums)<k:
            return len(nums)
        for r in range(l,len(nums)): #Given array is sorted
            if nums[r]!=nums[l-k]: #if current element is not equal to the previous K elements
                nums[l]=nums[r] #Than swap or delete the element
                l=l+1 #Increase K
        return nums[:l]


def main():
    nums=[1, 2, 2,2, 3,3, 4]
    nums=remove_duplicates_generic(nums)
    print(nums)


main()
