class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}  # HashMap to store indices of elements

        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target
            if complement in num_indices:  # If complement exists in the HashMap
                return [num_indices[complement], i]  # Return indices of current element and complement
            num_indices[num] = i  # Add current element and its index to the HashMap

        # If no solution is found
        return None

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
