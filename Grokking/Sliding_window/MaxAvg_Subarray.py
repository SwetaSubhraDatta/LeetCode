
class MaxAvg():
    def findMaxAverage(self,n:list,K):
        res=[]
        avg=[]
        for i in range(0,len(n)):
            res.append(n[i])
            if(len(res)==K):
                avg.append(sum(res)/K)
                res=res[1:]
        min_avg=max(avg)
        return min_avg

    def find_averages_of_subarrays(self,K, arr):
        result = []
        sum_, l = 0.0, 0
        for r in range(len(arr)):
            sum_ += arr[r]  # add the next element
            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            if r >= K - 1:
                result.append(sum_ / K)  # calculate the average
                sum_ -= arr[l]  # subtract the element going out
                l += 1  # slide the window ahead
        return result


solution=MaxAvg()
print(solution.findMaxAverage([1,2,3,4,5,6,7],7))

