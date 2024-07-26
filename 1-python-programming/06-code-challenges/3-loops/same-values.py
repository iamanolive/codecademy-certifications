def same_values(lst1, lst2):
  index_list = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      index_list.append(index)
  return index_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))