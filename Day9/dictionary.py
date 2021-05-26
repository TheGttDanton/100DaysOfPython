programming_dictionary = {
  "Bug": "An error that is not expected and prevents the program to run",
  "Function": "Code of block",
  "Loop": "over and over again"
}

bug = programming_dictionary["Bug"]
print(bug)


programming_dictionary["Closure"] = "similar to function"

print(programming_dictionary)



#loop in dictionary

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
