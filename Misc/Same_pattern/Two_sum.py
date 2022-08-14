# two sum

def two_sum(nums, target):
    brute_force(nums, target)

def brute_force(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] 
