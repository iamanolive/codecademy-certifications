def append_sum(my_list):
  for i in range(3):
    sum = my_list[-1] + my_list[-2]
    my_list.append(sum)
  return my_list

print(append_sum([1, 1, 2]))