#find the subarray with product less than K


def numSubarrayProductlessthanK(nums:list,k:int):
        res = 0
        l = 0
        product = 1
        for r in range(len(nums)): #For each element in the array
            product *= nums[r] #Multiply the product by the current element
            while l < r and product >= k: #If the product is greater than k or left hand side is less than right hand side
                product //= nums[l] #Divide the product by the left hand side element /removing the left hand side element
                l += 1 #Increase the left hand side
            if product < k: # only if the product is less than k
                res += r - l + 1 #Add the number of elements in the subarray
        return res


def main():
    numSubarrayProductlessthanK([10,5,2,6],100)

main()