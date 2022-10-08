#find the peak index in bitonic array

from  typing import List
def peakIndexInBItonicArray(arr:List[int]):
    print(method_1(arr))
    print(method_2(arr))

def method_1(arr):
    start,end=0,len(arr)-1
    while(start<end):
        #find mid
        mid=(start+end)//2
        #Comapare the next element with mid and go into the decreasing part of the array
        if arr[mid]>arr[mid+1]:
            end=mid
        else:
            start=mid+1
    return start

def method_2(arr):
    start,end=0,len(arr)-1
    while(start<end):
        mid=start+end//2
        #Compre the previous element with mid and go into the increasing part of the array
        if arr[mid]>arr[mid-1]:
            start=mid
        else:
            end=mid-1
    return start

if __name__=="__main__":
    arr=[1,3,8,12,4,2]
    peakIndexInBItonicArray(arr)