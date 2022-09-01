it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# finding the length of the above set it_companies
print("The length of the set it_companies is :", len(it_companies))
# Adding twitter to it_companies
it_companies.add("Twitter")
print("The updated set after adding twitter into it is :", it_companies)
# Inserting multiple IT companies at once to the set it_companies
mnc_companies = {'Cognizant', 'fis', 'Techpark', 'Mindtree'}
it_companies.update(mnc_companies)
print("The set after inserting multiple IT companies :", it_companies)
# Removing one item from the set it_companies
it_companies.remove('Facebook')
print("The set after removing facebook from it is :", it_companies)
# Joining the above A and B sets
C = A.union(B)
print("Set after joining A and B sets :", C)
x = A.intersection(B)
print("The set after intersection of A and B is :", x)
y = A.issubset(B)
print("A subset of B is :", y)
z = A.isdisjoint(B)
print(" Disjoint of A and B is :", z)
X = A.union(B)
print("Joining A with B is :", X)
Y = B.union(A)
print("Joining B with A is :", Y)
i = A.symmetric_difference(B)
print("The symmetric difference between A and B is :", i)
# Deleting the sets completely
A.clear()
B.clear()
print("The set A after deleting is :", A)
print("The set B after deleting is :", B)
# Finding length of age list
age_list = [22, 19, 24, 25, 26, 24, 25, 25]
print("The length of the above age list is :", len(age_list))
# Converting age list to age set
age_set = set(age_list)
print("After converting age list to age set :", age_set)


