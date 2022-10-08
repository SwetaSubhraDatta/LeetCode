def next_greater_element(smaller_nums:list,bigger_nums:list):
    res=[]
    mp_nums2={}
    #S1: Create a hashmap of indexes of bigger_nums
    for i in range(len(bigger_nums)):
        mp_nums2[bigger_nums[i]]=i
    #S2: Iterate over smaller_nums and find the next greater element in bigger_nums
    for i in range(len(smaller_nums)): #Go over bigger_nums
        #S2.1: Find the index of the current element in bigger_nums
        if smaller_nums[i] in mp_nums2:
            index=mp_nums2[smaller_nums[i]]
        else:
            continue
        
        if index+1==len(bigger_nums):
            res.append(-1)
            continue
        j=index+1
        while(j<len(bigger_nums)):
            if bigger_nums[j]>smaller_nums[i]:
                res.append(bigger_nums[j])
                break
            j+=1
        if j==len(bigger_nums):
            res.append(-1)
    return res

def if_valid_index(index:int,length_of_big_array:int):
    return index+1<length_of_big_array

def main():
    nums1=[4,1,2]
    nums2=[1,3,4,2]
    print(next_greater_element(nums1,nums2))
    nums1=[1,3,5,2,4]
    nums2=[6,5,4,3,2,1,7]
    print(next_greater_element(nums1,nums2))

main()

    