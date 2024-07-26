def remove_middle(my_list, start, end):
  result_list = my_list[:start] + my_list[end + 1:]
  return result_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))