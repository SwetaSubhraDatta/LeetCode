def move_zeroes_end(nums):
    count_index=0
    for i in range(len(nums)):
        if nums[i]!=0: #find the first non-zero element
            nums[i],nums[count_index]=nums[count_index],nums[i]
        count_index+=1
    return nums

def move_zeroes_front(nums):
    #[1,2,3,0,0]
    #[0,0,1,2,3]
    
    count_index=0 
    for curr in range(len(nums)-1,-1,-1):
        #non zero elements will come at the back
        if nums[curr]!=0:
            nums[curr],nums[count_index]=nums[count_index],nums[i]
        count_index+=1
    return nums


def main():
    print(move_zeroes_end([1,2,3,0,0]))
main()



