#find the smallest letter in the array that is larger than target

def next_greatest_letter(letters,target):
    l,r = 0, len(letters)-1
    while l <= r:
        mid=(r+l)//2
        if letters[mid] <= target:
            l=mid+1
        else:
            r=mid-1
    
    if l==len(letters):
        return letters[0]
    else:
        return letters[l]

def main():
    letters = ["c", "f", "j"]
    target = "a"
    print(next_greatest_letter(letters,target))
main()
