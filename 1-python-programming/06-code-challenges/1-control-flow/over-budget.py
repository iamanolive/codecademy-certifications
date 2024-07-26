# monthly budget
budget = 2000

# monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# total expenses
total = food_bill + electricity_bill + internet_bill + rent

# total vs budget
if total > budget:
  over_budget = True
else:
  over_budget = False


print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))