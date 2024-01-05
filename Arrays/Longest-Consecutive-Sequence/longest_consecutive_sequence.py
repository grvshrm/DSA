def longestConsecutiveSequence(nums, n):
# Complexity : Time - O(n), Space - O(n)
    if n == 0:
        return 0
    unique_nums = set(nums)
    longest = 1
    for i in unique_nums:
        if i - 1 not in unique_nums:
            cnt = 1
            x = i
            while x + 1 in unique_nums:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

"""def longestConsecutiveSequence(nums, n):
# Complexity : Time - O(n*log(n)), Space - O(1)
    if n == 0:
        return 0
    nums.sort()
    lastSmaller = float("-inf")
    cnt = 0
    longest = 1
    for i in range(n):
        if nums[i] - 1 == lastSmaller:
            cnt += 1
            lastSmaller = nums[i]
        elif lastSmaller != nums[i]:
            cnt = 1
            lastSmaller = nums[i]
        longest = max(longest, cnt)
    return longest"""

if __name__ == '__main__':
    nums = [100, 102, 101, 2, 4, 5, 1, 2, 3, 100, 102]
    print(longestConsecutiveSequence(nums, len(nums)))