def middle_element(my_list):
  length = len(my_list)
  if length % 2 == 0:
    sum = my_list[int(length / 2)] + my_list[int(length / 2) - 1]
    average = sum / 2
    return average
  else:
    return my_list[int(length / 2)]
    

print(middle_element([5, 2, -10, -4, 4, 5]))