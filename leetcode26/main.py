class Solution:
    def removeDuplicates(self, nums):
        nums_set = list(set(nums))
        for i in nums:
            if i in nums_set:
                nums_set.remove(i)
            else:
                nums.append(nums.pop(nums.index(i)))

        print(nums)


        # print(type(list(set(nums))[0]))
        return len(list(set(nums))), nums
        # for term in nums:

solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

