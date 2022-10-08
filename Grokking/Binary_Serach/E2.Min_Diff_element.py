#Given an array sorted in ascending order find the element that has the min difference with the givn key


def search_min_diff_element(arr, key):
    l,r=binary_search(arr,key)
    if r==-1:
        return arr[l]
    else:
        if abs(arr[l]-key)<abs(arr[r]-key):
            return arr[l]
        else:
            return arr[r]


def binary_search(arr, key):
    
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]==key:
            return mid,-1
        elif arr[mid]<key:
            l=mid+1
        else:
            r=mid-1
    return l,r

def main():
    arr,target=[4,6,10],17
    print(search_min_diff_element(arr,target))

main()