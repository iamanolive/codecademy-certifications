def every_three_nums(start):
  index = 0
  my_list = []
  for num in range(start, 101):
    if index % 3 == 0:
      my_list.append(num)
    index += 1
  return my_list

print(every_three_nums(91))