my_dict = {}

# Insertion
my_dict["name"] = "John Doe"
my_dict["age"] = 30
my_dict["gender"] = "male"

#Print
print(f"The inserted dictionary is {my_dict}")
# Search
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# Deletion
del my_dict["gender"]

print("Dictionary after deletion: ", my_dict)
