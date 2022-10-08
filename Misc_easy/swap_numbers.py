def solution(a):
    #Init sum
    sum_ =0
    i=0

    while(i<len(a)-1):
        #First Edge condition
        if i==0:
            sum_ = 0+a[i]+a[i+1]
            print("i is "+str(i)+"sum is "+str(sum_))
        elif i==len(a)-1:
            sum_ = a[i-1]+a[i]+0
            print("i is "+str(i)+"sum is "+str(sum_))
        else:
            sum_=a[i-1]+a[i]+a[i+1]
            print("i is "+str(i)+"sum is "+str(sum_))
        a[i]=sum_
        i+=1
    print ("The mutated array is ",a)

a= [ 4,5,-1,2,1]
solution(a)
