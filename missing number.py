class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


if __name__ == "__main__":
    nums = [3, 0, 1]

    obj = Solution()
    result = obj.missingNumber(nums)

    print(result)