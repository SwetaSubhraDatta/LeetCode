def findUnsortedSubarray(nums: list) -> int:
        sorted_nums = sorted(nums)
        if nums == sorted_nums:
            return 0
        start = n = len(nums)
        end = -1
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return (end - start + 1)


def main():
    print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

main()