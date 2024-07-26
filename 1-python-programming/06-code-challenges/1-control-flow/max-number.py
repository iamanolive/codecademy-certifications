def max_num(num1, num2, num3):
  if num1 == num2:
    return "It's a tie!"
  elif num1 == num3:
    return "It's a tie!"
  elif num2 == num3:
    return "It's a tie!"
  else:
    return max(num1, num2, num3)

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))