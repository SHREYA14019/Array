class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1

    obj = Solution()
    result = obj.threeSumClosest(nums, target)

    print(result)