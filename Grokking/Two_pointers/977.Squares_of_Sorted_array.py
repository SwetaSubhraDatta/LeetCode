#Create squares of sorted array

def create_squares(nums):
    for r in range(len(nums)):
        nums[r]=nums[r]**2
    nums.sort()
    return remove_duplicates(nums)# Just an additional thing to pratcice  on the concept of removal of duplicates from a sorted array

def remove_duplicates(nums):
    k=1
    l=k
    if len(nums)<k:
        return len(nums)
    for r in range(l,len(nums)):
        if nums[r]!=nums[l-k]:
            nums[l]=nums[r]
            l=l+1
    return nums[:l]
        


def main():
   print(create_squares(nums=[-1,-2,0,1,2]))

main()
