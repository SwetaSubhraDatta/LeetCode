
def search_in_mountain_array(arr, key):
    peak=find_peak(arr)
    found=Order_agnostic_binary_search(key,arr,0,peak) #search in the increasing part of the array
    if found==-1:
        found=Order_agnostic_binary_search(key,arr,peak+1,len(arr)-1) # if not found search in the decreasing part of the array
    return found

def Order_agnostic_binary_search(key,arr,start,end):
    #Check if ascending or descending
    isAsc=False
    if arr[start]<arr[end]:
        isAsc=True

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==key:
            return mid

        if isAsc:
            if arr[mid]>key:
                end=mid-1
            else:
                start=mid+1
        else:
            if key>arr[mid]:
                end=mid-1
            else:
                start=mid+1
        
    return -1

def find_peak(arr):
    start,end=0,len(arr)-1
    while start<end:
        mid=(start+end)//2
        if arr[mid]>arr[mid+1]:
            end=mid #go to the decreasing part of the array
        else:
            start=mid+1 #bring start pointer to the increasing part of the array
    return start

if __name__=="__main__":
    arr=[1,5,2]
    print(search_in_mountain_array(arr,2))
    print(search_in_mountain_array(arr,1))
    print(search_in_mountain_array(arr,3))



