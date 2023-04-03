class Solution:
    def searchInsert(self, nums, target):
        mid = len(nums) // 2
        if len(nums)==0:
            return mid
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            self.searchInsert(nums[:mid], target)
        else:
            self.searchInsert(nums[mid+1::], target)
solution = Solution()
print(solution.searchInsert([1, 3, 5, 6] ,5))