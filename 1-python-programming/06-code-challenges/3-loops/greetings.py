def add_greetings(names):
  my_list = []
  for name in names:
    greeting = "Hello, " + name
    my_list.append(greeting)
  return my_list

print(add_greetings(["Owen", "Max", "Sophie"]))