# Creating tuples
siblings = ("priya", "sravan")
print("My siblings are: ", siblings)
# Printing the length of the above tuple
print("The number of siblings I have are: ", len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
x = list(siblings)
x.append("vijaya")
x.append("ramesh")
siblings = tuple(x)
print("The updated tuple is :", siblings)

