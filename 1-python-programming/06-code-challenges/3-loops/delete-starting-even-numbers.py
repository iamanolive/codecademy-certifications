def delete_starting_evens(my_list):
  index = 0
  for num in my_list:
    if num % 2 == 0:
      index += 1
    else:
      break
  return my_list[index:]

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))