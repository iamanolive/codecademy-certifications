def odd_indices(my_list):
  new_list = []
  for i in range(len(my_list)):
    if i % 2 != 0:
      new_list.append(my_list[i])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))