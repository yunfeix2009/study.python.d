nums = [3, 2, 2, 3]
val=3
return_ls = []
for index in range(len(nums)):
    if nums[index] == val:
        nums.append(nums[index])
        nums.remove(nums[index])
    else:
        return_ls.append(nums[index])
print(nums)
print(return_ls)