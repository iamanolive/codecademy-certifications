def combine_sort(my_list1, my_list2):
  my_list = my_list1 + my_list2
  my_list.sort()
  return my_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))