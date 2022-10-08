# count all triplets in array that sum less than target
 
 
def threesumsmall_returnoutput(nums,target):
        g_ct = 0
        nums.sort()
        for i, num in enumerate(nums):

            l, r = i+1, len(nums)-1

            while l<r:

                sums = nums[l] + nums[r] +num

                if sums < target :
                    g_ct +=r-l
                    l+=1
                else:
                    r-=1

        return g_ct

def threeSumSmall_returntriplets(nums, target):
    nums.sort()
    res = []
    for x in range(len(nums) - 2):
        l, r = x + 1, len(nums) - 1
        while l < r:
            if nums[x] + nums[l] + nums[r] < target:
                for k in range(r,l,-1):
                    res.append([nums[x],nums[l],nums[k]])
                l += 1 
            else:
                r -= 1
    return res


def main():
    count=threeSumSmall_returntriplets([-1, 0, 2, 3],3)
    print(count)

main()
