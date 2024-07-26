def over_nine_thousand(lst):
  sum = 0
  for item in lst:
    sum += item
    if sum > 9000:
      return sum
  return sum


print(over_nine_thousand([8000, 900, 120, 5000]))