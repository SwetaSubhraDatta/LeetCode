#two sum
def twoSum_II_two_pointers(nums,target): #Only valid when the array is sorted
    l,r=0,len(nums)-1
    sum_=0
    while(l<r):
        sum_=nums[r]+nums[l]
        if sum_==target:
            return [l,r]
        if sum_>target: #if the sum is greater the
            r-=1
        else:
            l+=1
def twoSum(nums,target): #HaspMapn method works for both when the array is sorted and unsorted
    mp={} #Create a hashmap
    for c,i in enumerate(nums): #Enumerate gives the index and value of the array
        if i in mp: #If the value is in the hashmap
            return [mp[i],c] # return the index of the element and the index of the current element
        mp[target-i]=c # if the value is not there add it to the hashmap

def main():
    d=twoSum([2,3,4],6)
    print(d)

main()

