# Creating new dictionary named studentdict
studentdict = {
    "first_name":"supraja",
    "last_name":"bathula",
    "gender":"female",
    "age":"23",
    "marital_status":"unmarried",
    "skills": ["python"],
    "country":"USA",
    "city":"overland park",
    "address":"kansas city",
}
print("The length of the student dictionary is: ", len(studentdict))
# Getting the values of the "skills" key from the above dictionary.!
studentdict.get("skills")
print("The value of the skills key is: ", studentdict.get("skills"))
datatype= type(studentdict.get("skills"))
print("The datatype is: ", datatype)
studentdict["skills"].append("Java")
print("The value of the skills key is: ", studentdict.get("skills"))   # Get dictionary keys as a list
keys = list(studentdict.keys())
print(keys)           # Get dictionary values as a list
print("printing dictionary values as a list :", list(studentdict.values()))








