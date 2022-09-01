from statistics import median
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorting the above given list
ages.sort()
print(ages)
# Printing the minimum and maximum ages from the given above list
print('The minimum age in the list is: ', min(ages))
print('The maximum age in the list is: ', max(ages))
# Inserting min. and max. ages again to the list
ages.insert(0, min(ages))
ages.insert(10, max(ages))
print('The updated list is: ', ages)
# Finding median
print('The median value of the list is :', median(ages))
# Finding average of the list
print('Average of the list is: ', sum(ages))
# Finding the range of the given list
range_age = max(ages) - min(ages)
print('The range of the given list is: ', range_age)




