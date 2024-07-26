def max_num(nums):
  largest_num = nums[0]
  for num in nums:
    if num > largest_num:
      largest_num = num
  return largest_num

print(max_num([50, -10, 0, 75, 20]))