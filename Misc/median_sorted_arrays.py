#find median of two sorted arrays
class Solution():
    def findMedianSortedArrays(self, nums1:list, nums2:list)->float:
        nums1=nums1+nums2
        nums1.sort()
        length=len(nums1)
        if length%2==0:
            return (nums1[length//2]+nums1[length//2-1])/2
        else:
            return nums1[length//2]




soln=Solution()
a=[1,2,3]
b=[3,4,5]
print(soln.findMedianSortedArrays(a,b))
