import math
def smallest_subarray_sum(s, n):
  # TODO: Write your code here
  w_s,sum_= 0,0
  l=0
  min_length=math.inf
  for i in range(0,len(n)):
    sum_=sum_+n[i]
    l=l+1
    while(sum_>=s):
      min_length=min(min_length,l)
      sum_=sum_-n[w_s]
      w_s+=1
      l=l-1
  if min_length==math.inf:
    return 0
      
  return min_length


d=smallest_subarray_sum(7, [2, 3,1,2,4,3])
print(d)