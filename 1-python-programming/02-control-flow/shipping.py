weight = 41.5

# ground shipping
if weight <= 2:
  ground_shipping = 20 + (1.50 * weight)
elif weight <= 6:
  ground_shipping = 20 + (3.00 * weight)
elif weight <= 10:
  ground_shipping = 20 + (4.00 * weight)
else:
  ground_shipping = 20 + (4.75 * weight)
print("Ground Shipping: $", ground_shipping)

# ground shipping premium
premium_ground_shipping = 125.00
print("Premium Ground Shipping: $", premium_ground_shipping)

# drone shipping
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight <= 6:
  drone_shipping = weight * 9.00
elif weight <= 10:
  drone_shipping = weight * 12.00
else:
  drone_shipping = weight * 14.25
print("Drone Shipping: $", drone_shipping)