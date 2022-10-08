
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
        windowSum, windowStart = 0.0, 0
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]  # add the next element
            # slide the window, we don't need to slide if we've not hit the required window size of 'k'
            if windowEnd >= K - 1:
                result.append(windowSum / K)  # calculate the average
                windowSum -= arr[windowStart]  # subtract the element going out
                windowStart += 1  # slide the window ahead

        return result

        def findMaxAverage(self, nums: List[int], k: int) -> float:
        #Step1: First initialise  the result and the variables
            w_start=0
            sum_=0
            avg_list=[]
            for i in range(0,len(nums)):
                #Step2: find the sum until K is reached
                sum_=sum_+nums[i]
                if i>k-1:
                    #Step 3: Store the average
                    avg_list.append(sum_/k)
                    #Step 4: Most important optimisation step reuse the sum
                    sum_=sum_-nums[w_start]
                    #Step 5: increase the w_start pointer
                    w_start+=1
            return max(avg_list)

solution=MaxAvg()
print(solution.findMaxAverage([1,2,3,4,5,6,7],7))

